import socket


import pytest

ADDR: str = '127.0.0.1'
PORT: int = 8080

HOST: str = ADDR + ':' + str(PORT)

@pytest.fixture
def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    yield client_socket
    client_socket.close()


@pytest.fixture
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(
        (ADDR, PORT)
    )
    server_socket.listen()
    yield server_socket
    server_socket.close()
