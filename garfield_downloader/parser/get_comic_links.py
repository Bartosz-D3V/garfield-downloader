""" get_comic_links module

Defines functions used to generate
download links

"""

from datetime import date, timedelta
from typing import Generator

BASE_URL: str = "https://garfield.com/comic/"


def get_comic_links(start_date: date, end_date: date) -> Generator[str, None, None]:
    """
    Returns list of HTTP links leading to Garfield comics
    within given range
    :param start_date: date
    :param end_date: date
    :return: Generator
    """
    for date_counter in range(int((end_date - start_date).days + 1)):
        yield BASE_URL + date_to_url(start_date + timedelta(date_counter))


def date_to_url(date_val: date) -> str:
    """
    Convert date to YYYY/MM/DD str format
    :param date_val: date
    :return: string
    """
    return date_val.strftime('%Y/%m/%d')
