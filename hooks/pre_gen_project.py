#!/usr/bin/env python
"""Pre-generation hooks."""

import re
import sys

from click import echo

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug }}'

if not re.match(MODULE_REGEX, module_name):
    echo('ERROR: The project slug ({}) is not a valid Python module name. Please do not use a - and use _ instead'.
         format(module_name))

    # Exit to cancel project
    sys.exit(1)
