from typing import List

from src.enum.http_method_enum import HTTPMethodEnum


class HTTPRequest:

    CRLF: bytes = b'\r\n'

    def __init__(self, raw_data: bytes) -> None:
        self.data = raw_data
        self._request_method: str = self._extract_http_method()
        self._request_headers: dict = self._extract_headers()
        self._request_body: bytes = self._extract_body()

    def _extract_body(self):
        return self.data.split(self.CRLF * 2, maxsplit=1)[1]

    def _extract_headers(self):
        raw_header_list: List = self.data.decode().split(self.CRLF.decode())[1:]
        headers: dict = dict()
        for header in raw_header_list:
            if ': ' in header:
                header_key, header_value = header.split(': ', maxsplit=1)
                headers[header_key] = header_value
        return headers
    
    def _extract_http_method(self):
        raw_http_method: List[str] = self.data.decode().split()[0]
        http_method: str = HTTPMethodEnum.get_http_method_by_name(raw_http_method)
        return http_method

    @property
    def method(self):
        ...

    @method.getter
    def method(self):
        return self._request_method

    @property
    def headers(self):
        ...
    
    @headers.getter
    def headers(self):
        return self._request_headers

    @property
    def body(self):
        ...
    
    @body.getter
    def body(self):
        return self._request_body
