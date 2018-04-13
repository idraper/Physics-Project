import socket, keyboard

class MySocket:
	def __init__(self, sock=None):
		self.conn = None
		self.addr = None
		self.sock = socket.socket()

	def send(self, host, port, msg):
		self.sock.connect((host, port))
		self.sock.send(msg.encode())
		print ('sent: ' + str(msg))

	def recieve(self, host, port):
		self.sock.bind((host,port))
		print ('bound')
		self.sock.listen(1)
		self.conn, self.addr = self.sock.accept()
		print ("Connection from: " + str(self.addr))
		while True:
			data = self.conn.recv(1024).decode()
			if not data or keyboard.is_pressed('a'):
				break
			print ("recieved: " + str(data))
		self.conn.close()