from src.enum.content_type_enum import ContentTypeEnum


class ResponseObject:
    def __init__(self, body: str, content_type: ContentTypeEnum) -> None:
        self._body = body
        self._content_type = content_type
        self._content_length = self._calculat_content_length(body)

    @staticmethod
    def _calculat_content_length(body):
        return len(body)

    @property
    def content_length(self):
        ...
    
    @content_length.getter
    def content_length(self):
        return self._content_length

    @property
    def body(self): 
        ...
    
    @body.getter
    def body(self):
        return self._body
    
    @property
    def content_type(self):
        ...
    
    @content_type.getter
    def content_type(self):
        return self._content_type.value

