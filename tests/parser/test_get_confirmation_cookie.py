from httmock import urlmatch, response, HTTMock

from garfield_downloader.parser.get_confirmation_cookie import get_confirmation_data


@urlmatch(netloc=r'(.*\.)?garfield\.com$')
# pylint: disable=unused-argument
def garfield_mock(url, request) -> str:
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
        assert dict(res[1])['first'] == 'some_cookie_1'
