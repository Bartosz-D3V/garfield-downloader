""" Unit tests for get_confirmation_cookie
module
"""
from http.cookiejar import CookieJar

from httmock import urlmatch, response, HTTMock
from requests import Response
from requests.utils import dict_from_cookiejar

from garfield_downloader.parser.get_confirmation_cookie import get_confirmation_data, get_age_gated


@urlmatch(netloc=r'(.*\.)?garfield\.com$')
# pylint: disable=unused-argument
def garfield_mock(url, request) -> Response:
    """
    Mock HTTP response containing cookie and a HTML
    form with secret token input
    :param url: str
    :param request: Request
    :return: Response
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


@urlmatch(netloc=r'(.*\.)?garfield\.com$', path=r'^/agegate$', method="POST")
# pylint: disable=unused-argument
def garfield_age_gated_mock(url, request) -> Response:
    """
    Mock HTTP response containing cookie with
    age-gated information
    :param url: str
    :param request: Request
    :return: Response
    """
    headers = {
        'content-type': 'text/html',
        'Set-Cookie': 'age-gated=my_secret_cookie'
    }
    return response(status_code=200, headers=headers, request=request)


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


def test_get_age_gated() -> None:
    """
    get_age_gated should return string with a cookie
    age-gated
    :return: None
    """
    with HTTMock(garfield_age_gated_mock):
        res = get_age_gated('mock_security_token', CookieJar())
        assert res == 'my_secret_cookie'
