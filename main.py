import logging


from src.server.http import HTTPServer
from src.config.runtime_config import RuntimeConfig


if __name__ == '__main__':
    logging.basicConfig(level=RuntimeConfig.LOGGING_LEVEL)
    server = HTTPServer()
    server.start()
