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
    year, month, date = paths[6].split('?')[0].split('-')
    month_lit = datetime.date(1900, int(month), 1).strftime('%B')
    return f"{year}/{month_lit}/{date}"
