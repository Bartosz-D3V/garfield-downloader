""" get_imgs_src module

Defines get_imgs_src function

"""
from typing import List

import requests
from requests import Response

from bs4 import BeautifulSoup


def get_imgs_src(url: str, **kwargs) -> List[str]:
    """
    Fetches all src attributes from image elements
    within div with class comic-display
    :param url: str
    :param kwargs: ageGated
    :return: List[str]
    """
    res: Response = requests.get(url, cookies={'age-gated': kwargs.get('age_gated')})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    comic_el = soup.select('div.comic-display img')
    return list(map(lambda img: img['src'], comic_el))
