#!/usr/bin/python3
from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        print('enter')
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None
        print('exit')


from functools import partial
if __name__ == '__main__':	
	conn = LazyConnection(('www.python.org', 80))
	# Connection closed
	print('beforwith')
	with conn as s:
		  print('afterwith')
		  # conn.__enter__() executes: connection open
		  s.send(b'GET /index.html HTTP/1.0\r\n')
		  s.send(b'Host: www.python.org\r\n')
		  s.send(b'\r\n')
		  resp = b''.join(iter(partial(s.recv, 8192), b''))
		  print('36')
		  # conn.__exit__() executes: connection closed

	print('39')
	#上下文管理协议(with语句)。
