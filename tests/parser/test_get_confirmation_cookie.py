""" Unit tests for get_confirmation_cookie
module
"""

from httmock import urlmatch, response, HTTMock
from requests.utils import dict_from_cookiejar

from garfield_downloader.parser.get_confirmation_cookie import get_confirmation_data


@urlmatch(netloc=r'(.*\.)?garfield\.com$')
# pylint: disable=unused-argument
def garfield_mock(url, request) -> str:
    """
    Mock HTTP response containing cookie and a HTML
    form with secret token input
    :param url:
    :param request:
    :return:
    """
    content = """
    <html>
        <body>
            <input name='_token' value='secret_token'></input>
        </body>
    </html>
    """
    headers = {
        'content-type': 'text/html',
        'Set-Cookie': 'first=some_cookie_1'
    }
    return response(status_code=200, headers=headers, content=content, request=request)


def test_get_confirmation_data() -> None:
    """
    get_confirmation_data should return Tuple with
    security token and CookieJar
    :return: None
    """
    with HTTMock(garfield_mock):
        res = get_confirmation_data()
        assert res[0] == 'secret_token'
        assert dict_from_cookiejar(res[1])['first'] == 'some_cookie_1'
