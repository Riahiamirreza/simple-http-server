import logging


from src.server.tcp import TCPServer
from src.config.runtime_config import RuntimeConfig


if __name__ == '__main__':
    logging.basicConfig(level=RuntimeConfig.LOGGING_LEVEL)
    tcp_server = TCPServer()
    tcp_server.start()
