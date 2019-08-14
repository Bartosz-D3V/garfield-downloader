""" download_images module

Defines download_images function

"""

from collections.abc import Iterable

from garfield_downloader.file_util.create_dir import create_dir
from garfield_downloader.downloader.download_image import download_image
from garfield_downloader.downloader.get_comic_dir import get_comic_dir


def download_images(loc: str, links: Iterable) -> None:
    """
    Function to download all data from provided links
    :param loc: str
    :param links: Iterator
    :return: None
    """
    for src in links:
        save_dir = get_comic_dir(src)
        create_dir(f"{loc}/{'/'.join(save_dir.split('/')[:2])}")
        download_image(f"{loc}/{save_dir}", src)
