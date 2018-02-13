# -*- coding: utf-8 -*-
"""flake8-checkstyle - a flake8 plugin to output Checkstyle XML reports.

This formatter plugin output XML to stdout.
"""
from io import BytesIO
from xml.etree import cElementTree as ET

from flake8.formatting.base import BaseFormatter


#: The first matching prefix determines the severity(inconsistent: info).
CHECKSTYLE_SERVERITY = {
    'E': 'error',
    'W': 'warning',
}

#: The first matching prefix determines the source
#: (inconsistent: undefined code).
CHECKSTYLE_SOURCE = {
    'E': 'pycodestyle',
    'W': 'pycodestyle',
    'F': 'pyflakes',
    'C': 'mccabe',
    'H': 'hacking',
    'I': 'flake8-import-order',
    'D': 'flake8-docstrings',
}


class CheckstylePlugin(BaseFormatter):
    """A plugin for flake8 to output Checkstyle XML reports."""

    def __init__(self, options):
        """Initialize members."""
        super(CheckstylePlugin, self).__init__(options)
        self.errors = []
        self.checkstyle_element = ET.Element('checkstyle')

    def beginning(self, _):
        """Reset the per-file list of errors."""
        self.errors = []

    def handle(self, error):
        """Add an error to the end of the self.errors."""
        self.errors.append(error)

    def finished(self, filename):
        """Make Checkystyle ElementTree."""
        if len(self.errors) < 1:
            return

        element = ET.SubElement(self.checkstyle_element, 'file', name=filename)
        for error in self.errors:
            message = error.code + ' ' + error.text
            prefix = error.code.strip()[0]
            ET.SubElement(element, 'error', {
                'severity': CHECKSTYLE_SERVERITY.get(prefix, 'info'),
                'line': str(error.line_number),
                'column': str(error.column_number),
                'message': message,
                'source': CHECKSTYLE_SOURCE.get(prefix, 'undefined code'),
            }
            )

    def stop(self):
        """Output Checkstyle XML reports."""
        et = ET.ElementTree(self.checkstyle_element)
        f = BytesIO()
        et.write(f, encoding='utf-8', xml_declaration=True)
        xml = f.getvalue().decode('utf-8')
        if self.output_fd is None:
            print(xml)
        else:
            self.output_fd.write(xml)
        super(CheckstylePlugin, self).stop()  # closes output file
