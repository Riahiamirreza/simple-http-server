import json
import logging


from src.server.tcp import TCPServer
from src.constants.http_response import HTTPResponseConstants
from src.constants.http_headers import HTTPHeadersConstants
from src.enum.content_type_enum import ContentTypeEnum
from src.utils.response_object import ResponseObject


class HTTPServer(TCPServer):
    LINE_TERMINATOR: bytes = b'\r\n'

    def handle_request(self, data):
        response_line: str = self._get_response_line(data)
        response_object: ResponseObject = self._get_response_object(data)
        headers: dict = self._get_response_headers(data, response_object)
        
        response: bytes = self._construct_response(response_line, headers, response_object)
        print(response.decode())
        return response

    def _get_response_line(self, data) -> str:
        return HTTPResponseConstants.OK_200
    
    def _get_response_headers(self, data, response_object: ResponseObject) -> dict:
        headers: dict = {
            HTTPHeadersConstants.CONTENT_TYPE: response_object.content_type,
            HTTPHeadersConstants.CONTENT_LENGTH: response_object.content_length,
            HTTPHeadersConstants.CONNECTION: 'Closed'
        }
        return headers

    def _get_response_object(self, data) -> ResponseObject:
        body_dict: dict = {'name': 'Ali'}
        body: str = json.dumps(body_dict)
        content_type = ContentTypeEnum.APPLICATION_JSON
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
