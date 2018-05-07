#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setuptools script for flake8-checkstyle."""

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'flake8>=3.0.0'
]

test_requirements = [
    'tox',
    'pytest'
]

setup(
    name='flake8-checkstyle',
    version='0.1.2',
    description='Output Checkstyle XML reports of flake8 violations.',
    long_description=readme + '\n\n' + history,
    author='Daichi Kumagai',
    author_email='d9magai@gmail.com',
    url='https://github.com/d9magai/flake8-checkstyle',
    packages=[
        'flake8_checkstyle',
    ],
    package_dir={'flake8_checkstyle': 'flake8_checkstyle'},
    include_package_data=True,
    install_requires=requirements,
    license='MIT License',
    entry_points={
        'flake8.report': [
            'checkstyle = flake8_checkstyle:CheckstylePlugin',
        ]
    },
    zip_safe=False,
    keywords='flake8 checkstyle',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Flake8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
