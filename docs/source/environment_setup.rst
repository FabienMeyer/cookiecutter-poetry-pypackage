.. highlight:: shell

=================
Environment Setup
=================

The projects created using this template make use of Poetry_ and Tox_ to set up
environments.

Most of these environments are also supported by this package itself.

Poetry environment
------------------

The default environment created with Poetry_ allows to run ``tox`` and
``bump2version``::

    poetry install
    poetry run tox
    poetry run bump2version patch

Installing the ``test`` extra allows to also run ``pytest``::

    poetry install -E test
    poetry run pytest

Test environment
----------------

Tox_ creates environment for all the supported Python versions (e.g., Python
3.7). All these environments install the package with the ``test`` extra
in order to run the unit tests.

This environment can be used to configure the ``pytest`` path in external
tools::

    poetry run tox -e py37
    .tox/py37/Scripts/python.exe
    .tox/py37/Scripts/pytest.exe

Linting environment
-------------------

Tox_ can create an environment for each linting tool. A cumulative environment
is also available and to run ``yapf``, ``flake8``, ``isort``, ``mypy``, and
``doc8``.

This environment can be used to configure the linting tools' path in external
tools::

    poetry run tox -e linting
    .tox/linting/Scripts/yapf.exe
    .tox/linting/Scripts/flake8.exe
    .tox/linting/Scripts/isort.exe
    .tox/linting/Scripts/mypy.exe
    .tox/linting/Scripts/doc8.exe

Documentation environments
--------------------------

Tox_ can generate documentation with Sphinx_ and set up a local HTTP server::

    poetry run tox -e docs  # Generates the documentation in docs/build/html
    poetry run tox -e serve-docs  # Serves the documentation on localhost.

Release environments
--------------------

Tox_ can be used to automate building and publishing a package::

    poetry run tox -e release

The basic behavior is simple to achieve with ``poetry`` as well, but ``tox``
simplifies automation and customization.

Since this template is not a package, this feature is not available here, but
only for generated projects.


.. _Poetry: https://python-poetry.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
