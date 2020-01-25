#!/usr/bin/env python
"""Tests for `{{ cookiecutter.project_slug }}` package."""

import pytest

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


@pytest.fixture
def name():
    # type: () -> str
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return 'World'


def test_content(name):
    # type: (str) -> None
    """Sample pytest test function with the pytest fixture as an argument."""
    assert 'Hello World' in {{ cookiecutter.project_slug }}.hello(name)
