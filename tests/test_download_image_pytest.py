import filecmp

import os

from downloader.download_image import download_image

url = 'https://python.org/static/community_logos/python-logo-master-v3-TM-flattened.png'


def test_download_image_should_save_image(tmpdir):
    tmpdir.mkdir('temp')
    download_image(tmpdir.get_temproot(), url)

    assert filecmp.cmp(
        f'{tmpdir.get_temproot()}/python-logo-master-v3-TM-flattened.png',
        f'{os.path.dirname(os.path.abspath(__file__))}/resources/python-logo.png')
