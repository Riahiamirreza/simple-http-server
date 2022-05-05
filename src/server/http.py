import json
import logging


from src.server.tcp import TCPServer
from src.config.runtime_config import RuntimeConfig
from src.constants.http_response import HTTPResponseConstants
from src.constants.http_headers import HTTPHeadersConstants
from src.enum.content_type_enum import ContentTypeEnum
from src.enum.http_method_enum import HTTPMethodEnum
from src.utils.response_object import ResponseObject
from src.request.http import HTTPRequest


class HTTPServer(TCPServer):
    LINE_TERMINATOR: bytes = b'\r\n'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root_dir = RuntimeConfig.SERVER_ROOT_DIR

    def handle_request(self, raw_data):
        request = HTTPRequest(raw_data)

        # log request inf:
        logging.info(str(request))

        match request.method:
            case HTTPMethodEnum.HTTP_GET.value:
                response: bytes = self.handle_GET(request)

            case HTTPMethodEnum.HTTP_POST.value:
                response = self.handle_POST(request)

            case _:
                raise NotImplementedError

        print(response.decode())
        return response

    def handle_GET(self, request) -> bytes:
        response_line: str = self._get_response_line(request)
        response_object: ResponseObject = self._get_response_object(request)
        headers: dict = self._get_response_headers(request, response_object)
        
        response: bytes = self._construct_response(response_line, headers, response_object)
        return response

    def handle_POST(self, request):
        ...

    def _get_response_line(self, request) -> str:
        return HTTPResponseConstants.OK_200
    
    def _get_response_headers(self, request, response_object: ResponseObject) -> dict:
        headers: dict = {
            HTTPHeadersConstants.CONTENT_TYPE: response_object.content_type,
            HTTPHeadersConstants.CONTENT_LENGTH: response_object.content_length,
            HTTPHeadersConstants.CONNECTION: 'Closed'
        }
        return headers

    def _get_response_object(self, request) -> ResponseObject:
        # body_dict: dict = {'name': 'Ali'}
        body: str = """<html>
            <body>
            <h1>Request received!</h1>
            <body>
            </html>
        """
        content_type = ContentTypeEnum.TEXT_HTML
        response_object = ResponseObject(body, content_type)
        return response_object

    @staticmethod
    def _construct_response(response_line: str, headers: dict, 
                            response_object: ResponseObject) -> bytes:
        response_line: bytes = response_line.encode() + HTTPServer.LINE_TERMINATOR
        headers: bytes = ''.join(
            [header[0] + ': ' + str(header[1]) + HTTPServer.LINE_TERMINATOR.decode() for header in headers.items()]
        ).encode()

        blank: bytes = HTTPServer.LINE_TERMINATOR
        response_body: bytes = response_object.body.encode()

        return b''.join([response_line, headers, blank, response_body])
