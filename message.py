# You can communicate with others through sockets
# message.py

import socket

sock = socket.socket()

class message:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket()
        else:
            self.sock = sock

    def serve(self, host=socket.gethostname(), port=8080):
	self.sock.bind((host, port))

    def send_msg(self, msg):
        self.sock.send(msg)

    def recv_msg(self):
        msg = ''
        while len(msg) < MSGLEN:
            chunk = self.sock.recv(MSGLEN-len(msg))
            if chunk == '':
                raise RuntimeError("socket connection broken")
            msg = msg + chunk	
        return msg

