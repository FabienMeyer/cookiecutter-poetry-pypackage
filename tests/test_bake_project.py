"""Baking tests."""

import datetime
import os
import shlex
import subprocess
from contextlib import contextmanager
from typing import TYPE_CHECKING
from typing import Iterator

if TYPE_CHECKING:
    from pytest_cookies import Cookies


@contextmanager
def inside_dir(dirpath):
    # type: (str) -> Iterator[None]
    """Execute code from inside the given directory.

    :param dirpath: Path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def run_inside_dir(command, dirpath):
    # type: (str, str) -> int
    """Run a command from inside a given directory, returning the exit status.

    :param command: Command that will be executed
    :param dirpath: Path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def test_year_compute_in_license_file(cookies):
    # type: (Cookies) -> None
    """Check that the license year is up to date."""
    result = cookies.bake(extra_context={'license': 'MIT license'})
    license_file_path = result.project.join('LICENSE')
    now = datetime.datetime.now()
    assert str(now.year) in license_file_path.read()


def test_bake_with_defaults(cookies):
    # type: (Cookies) -> None
    """Check the default arguments."""
    result = cookies.bake()
    assert result.project.isdir()
    assert result.exit_code == 0
    assert result.exception is None

    found_toplevel_files = [f.basename for f in result.project.listdir()]
    assert 'pyproject.toml' in found_toplevel_files
    assert 'python_boilerplate' in found_toplevel_files
    assert 'tox.ini' in found_toplevel_files
    assert 'tests' in found_toplevel_files


def test_bake_and_run_tests(cookies):
    # type: (Cookies) -> None
    """Check the default tests."""
    result = cookies.bake()
    assert result.project.isdir()
    assert run_inside_dir('pytest', str(result.project)) == 0


def test_bake_with_special_chars_and_run_tests(cookies):
    # type: (Cookies) -> None
    """Ensure that a `full_name` with double quotes does not break anything."""
    result = cookies.bake(extra_context={'full_name': 'name "quote" name'})
    assert result.project.isdir()
    assert run_inside_dir('pytest', str(result.project)) == 0


def test_bake_with_apostrophe_and_run_tests(cookies):
    # type: (Cookies) -> None
    """Ensure that a `full_name` with apostrophes does not break anything."""
    result = cookies.bake(extra_context={'full_name': "O'connor"})
    assert result.project.isdir()
    assert run_inside_dir('pytest', str(result.project)) == 0


def test_bake_open_source(cookies):
    # type: (Cookies) -> None
    """Ensure that the license is set correctly."""
    result = cookies.bake(extra_context={'license': 'MIT license'})
    assert 'MIT License' in result.project.join('LICENSE').read()
    assert 'MIT license' in result.project.join('README.rst').read()
    assert 'license = "MIT"' in result.project.join('pyproject.toml').read()


def test_bake_not_open_source(cookies):
    # type: (Cookies) -> None
    """Ensure that the license is set correctly."""
    result = cookies.bake(extra_context={'license': 'KB license'})
    found_toplevel_files = [f.basename for f in result.project.listdir()]
    assert 'pyproject.toml' in found_toplevel_files
    assert 'LICENSE' not in found_toplevel_files
    assert '**TBD** license' in result.project.join('README.rst').read()
    assert 'license = ' not in result.project.join('pyproject.toml').read()
