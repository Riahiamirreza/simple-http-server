import threading
import signal

from src.server.tcp import TCPServer

from tests.server.fixture import client


class TestTCPServer:

    @staticmethod
    def _start_server(server):
        thr = threading.Thread(target=server.start, args=(), kwargs={})
        thr.start()
        return thr
    
    def test_creaing_socket_object(self):
        host = '127.0.0.1'
        port = 12345
        tcp_server = TCPServer(host=host, port=port)
        assert tcp_server.socket_name == host + ':' + str(port) 

    def test_connecting_to_tcp_server(self, client):
        host = '127.0.0.1'
        port = 12345
        tcp_server = TCPServer(host=host, port=port)
        running_server = self._start_server(tcp_server)
        client.connect((host, port))
        running_server.join()
 
