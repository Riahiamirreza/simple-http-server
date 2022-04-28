import logging


from src.tcp_server.tcp_server import TCPServer
from src.config.runtime_config import RuntimeConfig


if __name__ == '__main__':
    logging.basicConfig(level=RuntimeConfig.LOGGING_LEVEL)
    tcp_server = TCPServer()
    tcp_server.start()
