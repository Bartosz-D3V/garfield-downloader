""" Unit tests for get_comic_dir module
"""

from garfield_downloader.downloader.get_comic_dir import get_comic_dir

URL_1 = 'https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/2019/2019-08-08.gif?v=1.1'


def test_get_comic_dir_should_construct_dir_path():
    """
    get_comic_dir should return directory path
    constructed from url
    :return:
    """
    dir_path = get_comic_dir(URL_1)

    assert dir_path == '2019/August/08.gif'
