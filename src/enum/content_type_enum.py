from enum import Enum, unique
from typing import Tuple


@unique
class ContentTypeEnum(Enum):
    APPLICATION_JSON: str = 'application/json'
    APPLICATION_JAVASCRIPT: str = 'application/javascript'
    APPLICATION_XML: str = 'application/xml'
    TEXT_HTML: str = 'text/html'


if __name__ == '__main__':
    a = ContentTypeEnum.APPLICATION_JAVASCRIPT
    print(a.value)