=============================
Cookiecutter Poetry PyPackage
=============================

Cookiecutter_ template for a Python package.

* Github repo: https://github.com/FabienMeyer/cookiecutter-poetry-pypackage

Features
--------

* Poetry_ project
* Formatting setup with ``yapf``
* Linting setup with ``flake8`` and ``mypy``
* Testing setup with ``pytest``
* Tox_ testing: Setup to easily test for Python 2.7, 3.5+
* Sphinx_ docs: Documentation ready for generation
* bump2version_: Pre-configured version bumping with a single command

Quick start
-----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/FabienMeyer/cookiecutter-poetry-pypackage

Then:

* Create a repo and put it there.
* Install the dev requirements into a virtual environment. (``poetry install``)

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _Poetry: https://python-poetry.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _bump2version: https://github.com/c4urself/bump2version
