import os

from pipenv.vendor import requests
from pipenv.vendor.requests import Response


def download_image(loc: str, url: str) -> None:
    res: Response = requests.get(url)
    res.raise_for_status()
    with open(os.path.join(loc, os.path.basename(url).split("?")[0]),
              'w+b') as image_file:
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
