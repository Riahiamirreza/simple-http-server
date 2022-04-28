
class HTTPResponseConstants:
    # 2xx
    OK_200: str = 'HTTP/1.1 200 OK'
    CREATED_201: str = 'HTTP/1.1 201 Created'
    ACCEPTED_202: str = 'HTTP/1.1 202 Accepted'

    # 3xx
    MOVED_PERMANENTLY_301: str = 'HTTP/1.1 301 Moved Permanently'

    # 4xx
    BAD_REQUEST_400: str = 'HTTP/1.1 400 Bad Request'
    UNAUTHORIZED_401: str = 'HTTP/1.1 401 Unauthorized'
    NOT_FOUND_404: str = 'HTTP/1.1 404 Not Found'

    # 5xx
    INTERNAL_SERVER_ERROR_500: str = 'HTTP/1.1 500 Internal Server Error'
