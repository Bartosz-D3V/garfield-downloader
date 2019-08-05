""" Unit tests for get_imgs_src module
"""

from httmock import urlmatch, HTTMock

from garfield_downloader.parser.get_imgs_src import get_imgs_src


@urlmatch(netloc=r'(.*\.)?garfield\.com$')
def garfield_mock(url, request) -> str:
    """
    Mock HTTP response using HTTMock
    :param url: HTTPMock url
    :param request: HTTPMock request
    :return: str
    """
    return """
    <html>
        <body>
            <div class="comic-display">
                <img src="first_href"></img>
            </div>
            <div class="comic-display">
                <img src="second_href"></img>
            </div>
        </body>
    </html>
    """


def test_get_imgs_src_should_return_srcs():
    """
    get_imgs_src should extract list of src
    attributes from a website inside dic.comic-display
    element
    :return: None
    """
    with HTTMock(garfield_mock):
        found_hrefs = get_imgs_src('https://garfield.com', age_gated='test')
        expected_hrefs = ["first_href", "second_href"]
        assert found_hrefs == expected_hrefs
