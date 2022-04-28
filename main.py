import logging


from src.server.http import HTTPServer
from src.config.runtime_config import RuntimeConfig


if __name__ == '__main__':
    logging.basicConfig(level=RuntimeConfig.LOGGING_LEVEL)
    server = HTTPServer(host='127.0.0.1', port=8080)
    server.start()
