from src.server.tcp import TCPServer


class TestTCPServer:
    
    def test_creaing_socket_object(self):
        host = '127.0.0.1'
        port = 12345
        tcp_server = TCPServer(host=host, port=port)
        assert tcp_server.socket_name == host + ':' + str(port) 

