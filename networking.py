import socket, keyboard

class MySocket:
	def __init__(self, sock=None):
		self.conn = None
		self.addr = None
		if sock is None:
			self.sock = socket.socket( \
							socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock

	def connect(self, host, port):
		self.sock.connect((host, port))

	def send(self, msg):
		self.conn.send(msg.encode())

	def recieve(self):
		self.sock = socket.socket()
		self.sock.bind(('',5040))
		self.sock.listen(1)
		self.conn, self.addr = self.sock.accept()
		print ("Connection from: " + str(addr))
		while True:
			data = self.conn.recv(1024).decode()
			if not data or keyboard.is_pressed('a'):
				break
			print ("recieved: " + str(data))
		self.conn.close()