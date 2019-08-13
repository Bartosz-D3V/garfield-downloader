""" Unit tests for download_images module
"""

from garfield_downloader.downloader.download_images import download_images

URL_1 = 'https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/2019/2019-08-08.gif?v=1.1'
URL_2 = 'https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/2018/2018-05-18.gif?v=1.1'
URL_3 = 'https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/2017/2017-01-29.gif?v=1.1'
URLS = (URL_1, URL_2, URL_3)


def test_download_images_should_download_images(tmpdir) -> None:
    """
    download_images should download all images into given
    directory
    :param tmpdir: pytest temporary directory
    :return: None
    """
    tmpdir.mkdir('test-download')
    download_images(f"{tmpdir.get_temproot()}/test-download", URLS)
