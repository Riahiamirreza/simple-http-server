from enum import Enum, unique


@unique
class HTTPMethodEnum(Enum):
    HTTP_GET: str = 'GET'
    HTTP_POST: str = 'POST'
    HTTP_PUT: str = 'PUT'
    HTTP_DELETE: str = 'DELETE'

    @classmethod
    def get_http_method_by_name(cls, http_method_name: str):
        if not isinstance(http_method_name, str):
            raise TypeError
        
        for member in cls.__members__.values():
            if member.value == http_method_name:
                return member.value
        else:
            raise ValueError
