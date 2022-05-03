import logging


from src.server.http import HTTPServer
from src.config.runtime_config import RuntimeConfig


def run_server(host: str, port: int):
    server = HTTPServer(host=host, port=port)
    server.start()
    server.end()


if __name__ == '__main__':
    logging.basicConfig(level=RuntimeConfig.LOGGING_LEVEL)
    run_server(host='127.0.0.1', port=8080)
