import socket


import pytest


@pytest.fixture
def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    yield client_socket
    client_socket.close()

