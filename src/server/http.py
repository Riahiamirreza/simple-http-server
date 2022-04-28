from src.server.tcp import TCPServer
from src.constants.http_response_constants import HTTPResponseConstants


class HTTPServer(TCPServer):
    LINE_TERMINATOR: bytes = b'\r\n'

    def handle_request(self, data):
        response_line: str = self._get_response_line(data)
        headers: dict = ...
        

    def _get_response_line(self, data) -> str:
        return HTTPResponseConstants.OK_200
    
    def _get_response_headers(self, data) -> dict:
        ...

    def _get_response_body(self, data) -> str:
        ...

