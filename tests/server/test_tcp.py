import threading
import signal

from src.server.tcp import TCPServer

from tests.server.fixture import client


class TestTCPServer:

    @staticmethod
    def _start_server(server):
        thr = threading.Thread(target=server.start, args=(), kwargs={})
        thr.daemon = True
        thr.start()
        return thr
    
    def test_creaing_socket_object(self):
        host = '127.0.0.1'
        port = 12345
        tcp_server = TCPServer(host=host, port=port)
        assert tcp_server.socket_name == host + ':' + str(port) 

    def test_connecting_to_tcp_server(self, client):
        host = '127.0.0.1'
        port = 12344
        tcp_server = TCPServer(host=host, port=port)
        running_server = self._start_server(tcp_server)
        client.connect((host, port))
        # client.close()
        # tcp_server.socket.close()

    def test_receive_sending_data(self, client):
        host = '127.0.0.1'
        port = 12349
        tcp_server = TCPServer(host=host, port=port)
        running_server = self._start_server(tcp_server)
        client.connect((host, port))
        message: bytes = b'hello server!'
        client.sendall(message)
        response = client.recv(1024)
        assert message == response
        # client.close()
        # tcp_server.socket.close()

        
