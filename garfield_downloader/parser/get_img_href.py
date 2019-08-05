from typing import List

import bs4
import requests
from requests import Response


def get_img_href(url: str, **kwargs) -> List[str]:
    res: Response = requests.get(url, cookies=kwargs.get('age-gated'))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comic_el = soup.select('div.comic-display img')
    hrefs = []
    for image in comic_el:
        hrefs.append(image['src'])
    return hrefs
