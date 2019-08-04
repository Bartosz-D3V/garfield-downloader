""" download_image module

Defines download_image function

"""

import os

import requests
from requests import Response


def download_image(loc, url: str) -> None:
    """
    :param loc: location (directory) to save the file
    :param url: location (HTTP address) of the image
    :return: None
    """
    res: Response = requests.get(url)
    res.raise_for_status()
    with open(os.path.join(loc, os.path.basename(url).split("?")[0]),
              'w+b') as image_file:
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
