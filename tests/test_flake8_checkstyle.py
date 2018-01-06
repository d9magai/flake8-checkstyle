#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the flake8 Checkstyle plugin."""

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import optparse
import sys

from flake8_checkstyle import CheckstylePlugin

from flake8.style_guide import Violation


def options(**kwargs):
    """Create an optparse.Values instance."""
    kwargs.setdefault('output_file', None)
    return optparse.Values(kwargs)


def test_handle():
    """Verify that a formatter will call format from handle."""
    formatter = CheckstylePlugin(options(show_source=False))
    error = Violation(
        code='A001',
        filename='example.py',
        line_number=1,
        column_number=1,
        text='Fake error',
        physical_line='a = 1',
    )

    formatter.handle(error)
    formatter.finished('example.py')
    io = StringIO()
    sys.stdout = io
    formatter.stop()
    sys.stdout = sys.__stdout__
    assert io.getvalue() == '<?xml version=\'1.0\' encoding=\'utf-8\'?>\n<checkstyle><file name="example.py"><error column="1" line="1" message="A001 Fake error" severity="info" source="undefined code" /></file></checkstyle>\n'
