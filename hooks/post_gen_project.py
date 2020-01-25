#!/usr/bin/env python
"""Post-generation hooks."""

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

project_license = '{{ cookiecutter.license }}'


def remove_file(filepath):
    # type: (str) -> None
    """Remove a file from the project directory."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if 'KB license' == project_license:
    remove_file('LICENSE')
