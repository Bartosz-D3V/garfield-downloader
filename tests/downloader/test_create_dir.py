""" Unit tests for create_dir module
"""

import os

from garfield_downloader.downloader.create_dir import create_dir


def test_create_dir_should_create_dir(tmpdir) -> None:
    """
    create_dir should create a new directory if
    it does not already exist in the given location
    :param tmpdir: pytest temporary directory
    :return: None
    """
    create_dir(f"{tmpdir.get_temproot()}/Test/SubFolder")
    assert os.path.exists(f"{tmpdir.get_temproot()}/Test/SubFolder")


def test_create_dir_should_not_create_dir(tmpdir) -> None:
    """
    create_dir should skip creating a new directory if
    it does already exist in the given location
    :param tmpdir: pytest temporary directory
    :return: None
    """
    tmpdir.mkdir('Test')
    create_dir(f"{tmpdir.get_temproot()}/Test")
    assert os.path.exists(f"{tmpdir.get_temproot()}/Test")
