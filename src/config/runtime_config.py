import logging


class RuntimeConfig:
    LOGGING_LEVEL = logging.INFO
    DEFAULT_PORT: int = 8080
    HOST_ADDRESS: str = '0.0.0.0'
