""" get_comic_dir module

Defines function used to generate
a relative filepath from URL
using date as discriminator

"""

import datetime


def get_comic_dir(url: str) -> str:
    """
    Returns relative directory path
    using encoded date in URL
    :param url: str
    :return: str
    """
    paths = url.split('/')
    date_split = paths[6].split('-')
    year = date_split[0]
    month = date_split[1]
    date = date_split[2].split('?')[0]
    month_lit = datetime.date(1900, int(month), 1).strftime('%B')
    return f"{year}/{month_lit}/{date}"
