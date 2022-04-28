from src.server.tcp import TCPServer
from src.constants.http_response import HTTPResponseConstants
from src.constants.http_headers import HTTPHeadersConstants


class HTTPServer(TCPServer):
    LINE_TERMINATOR: bytes = b'\r\n'

    def handle_request(self, data):
        response_line: str = self._get_response_line(data)
        response_object = self._get_response_body(data)
        headers: dict = self._get_response_headers(data)
        

    def _get_response_line(self, data) -> str:
        return HTTPResponseConstants.OK_200
    
    def _get_response_headers(self, data) -> dict:
        headers: dict = {}
        return headers

    def _get_response_body(self, data) -> str:
        ...

