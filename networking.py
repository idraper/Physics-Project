import socket, keyboard

class MySocket:
	def __init__(self, sock=None):
		self.conn = None
		self.addr = None
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self, host, port):
		self.sock.connect((host, port))

	def send(self, msg):
		self.sock.send(msg.encode())

	def recieve(self, host, port):
		self.sock = socket.socket()
		self.sock.bind((host,port))
		print ('bound')
		self.sock.listen(1)
		self.conn, self.addr = self.sock.accept()
		print ("Connection from: " + str(addr))
		while True:
			data = self.conn.recv(1024).decode()
			if not data or keyboard.is_pressed('a'):
				break
			print ("recieved: " + str(data))
		self.conn.close()