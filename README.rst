.. image:: https://circleci.com/gh/d9magai/flake8-checkstyle/tree/master.svg?style=svg
    :target: https://circleci.com/gh/d9magai/flake8-checkstyle/tree/master

==================
flake8-checkstyle
==================

Output Checkstyle XML reports of flake8 violations.

Quick Start
--------------

.. code-block:: bash

  $ pip install flake8-checkstyle

To print a Checkstyle report, use the ``--format=checkstyle`` command line argument. 

.. code-block:: bash

  $ flake8 --format=checkstyle path/to/code

The output will look like this:

.. code-block:: xml

  <?xml version='1.0' encoding='utf-8'?>
  <checkstyle>
    <file name="example.py">
      <error column="1" line="3" message="H306: imports not in alphabetical order (sys, os)" severity="info" source="hacking"/>
      <error column="1" line="3" message="I100 Import statements are in the wrong order. import os should be before import sys" severity="info" source="flake8-import-order"/>
      <error column="27" line="4" message="F821 undefined name 'index'" severity="info" source="pyflakes"/>
      <error column="1" line="7" message="E302 expected 2 blank lines, found 1" severity="error" source="pycodestyle"/>
      <error column="1" line="7" message="D101 Missing docstring in public class" severity="info" source="flake8-docstrings"/>
      <error column="20" line="7" message="W291 trailing whitespace" severity="warning" source="pycodestyle"/>
    </file>
  </checkstyle>

Checkstyle rule
----------------

flake8-checkstyle can coexist with other flake8 plugins.
The prefix code determines source and severity.

============  =====================  =========
prefix code   source                 severity
============  =====================  =========
E             pycodestyle            error
W             pycodestyle            warning
F             pyflakes               info
C             mccabe                 info
H             hacking                info
I             flake8-import-order    info
D             flake8-docstrings      info
============  =====================  =========

License
-------

* MIT License
