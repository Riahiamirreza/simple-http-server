import socket


import pytest


@pytest.fixture
def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client_socket


