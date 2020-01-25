"""Main module."""


def hello(name):
    # type: (str) -> str
    """Say hello.

    >>> hello('{{ cookiecutter.project_name }}')
    'Hello {{ cookiecutter.project_name }}!'
    """
    return 'Hello {}!'.format(name)
