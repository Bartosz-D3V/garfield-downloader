import filecmp

from downloader.download_image import download_image


def test_download_image_should_save_image(tmpdir):
    url = 'https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png'
    tmpdir.mkdir('temp')
    download_image(tmpdir.get_temproot(), url)

    assert filecmp.cmp(f'{tmpdir.get_temproot()}/python-logo-master-v3-TM-flattened.png',
                       './resources/python-logo.png')
