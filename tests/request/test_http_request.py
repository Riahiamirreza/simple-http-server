from src.request.http import HTTPRequest


class TestHTTPRequest:
    def test_get_http_method_GET(self):
        request = open('tests/request/samples/request_GET_1.sample', 'rb').read()
        http_request = HTTPRequest(request)

        assert http_request.method == 'GET'

    def test_get_http_method_POST(self):
        request = open('tests/request/samples/request_POST_1.sample', 'rb').read()
        http_request = HTTPRequest(request)

        assert http_request.method == 'POST'

    def test_get_http_method_PUT(self):
        request = open('tests/request/samples/request_PUT_1.sample', 'rb').read()
        http_request = HTTPRequest(request)

        assert http_request.method == 'PUT'

    def test_get_uri_1(self):
        request = open('tests/request/samples/request_GET_uri_1.sample', 'rb').read()
        http_request = HTTPRequest(request)

        assert http_request.uri == '/hello/uri'

    def test_get_uri_2(self):
        request = open('tests/request/samples/request_GET_uri_2.sample', 'rb').read()
        http_request = HTTPRequest(request)

        assert http_request.uri == '/hello/world/uri'
