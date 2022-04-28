import logging
import socket


class TCPServer:
    SOCKET_NAME_FORMAT: str = '{host}:{port}'
    ADDRESS_FORMAT: str = '{host}:{port}'
    RECEIVING_SIZE: int = 1024 * 1024

    def __init__(self, host: str = '127.0.0.1', port: int = 8080):
        self.host = host
        self.port = port
        self.socket = self._make_socket_object()

    def _make_socket_object(self):
        socket_object = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )
        socket_object.bind((self.host, self.port))
        socket_object.listen()
        return socket_object

    def start(self):
        logging.info('Start litening at: ' + self.socket_name) 
        try:
            while True:
                connection, addr = self.socket.accept()
                logging.info(f'Address {self.format_address(addr)} connected.')
                data = connection.recv(self.RECEIVING_SIZE)
                logging.info(data)
                response = self.handle_request(data)
                connection.sendall(data)
                connection.close()
        except KeyboardInterrupt:
            self.socket.close()

            
    def handle_request(self, raw_data):
        return raw_data
           
    @property
    def socket_name(self):
        ...

    @socket_name.getter
    def socket_name(self):
        host, port = self.socket.getsockname()
        return self.SOCKET_NAME_FORMAT.format(
            host=host, port=str(port)
        )

    @staticmethod
    def format_address( addr):
        host, port = addr
        return TCPServer.ADDRESS_FORMAT.format(
            host=host, port=str(port)
        )


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    server = TCPServer()
    server.start()
