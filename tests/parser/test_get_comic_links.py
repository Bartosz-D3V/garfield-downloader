""" Unit tests for get_img_hrefs module
"""

import datetime

from garfield_downloader.parser.get_comic_links import date_to_url, get_comic_links


def test_get_comic_links_should_return_links() -> None:
    """
    get_comic_links should return list of HTTP URLs
    to garfield comics within given range
    :return:
    """
    start_date = datetime.date(2020, 5, 30)
    end_date = datetime.date(2020, 6, 2)
    expected_list = [
        'https://garfield.com/comic/2020/05/30',
        'https://garfield.com/comic/2020/05/31',
        'https://garfield.com/comic/2020/06/01',
        'https://garfield.com/comic/2020/06/02',
    ]
    assert list(get_comic_links(start_date, end_date)) == expected_list


def test_date_to_url_should_return_str() -> None:
    """
    date_to_url should convert date to YYYY/MM/DD
    str format
    :return:
    """
    date = datetime.date(2020, 5, 17)
    assert date_to_url(date) == '2020/05/17'
