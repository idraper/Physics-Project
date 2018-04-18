import socket
from time import sleep

class MySocket:
	def __init__(self, sock=None):
		self.conn = None
		self.addr = None
		self.sock = socket.socket()
		
	def connect(self, host, port):
		self.sock.connect((host, port))
		
	def close(self):
		self.sock.close()

	def send(self, msg):
		try:
			self.sock.send(str(msg).encode())
		except AttributeError:
			self.sock.send(msg)
		print ('sent: ' + str(msg))

	def recieve(self, host, port):
		self.sock.bind((host,port))
		print ('bound')
		self.sock.listen(1)
		self.conn, self.addr = self.sock.accept()
		print ("Connection from: " + str(self.addr))
		data = []
		while True:
			d = self.conn.recv(1024).decode()
			if not d:
				break
			#print ("recieved: " + str(d))
			data.append(d)
		self.conn.close()
		return data
		
	def sendKey(self, key):
		self.send(key.scramble(len(key.getMessageListFull())))
		sleep(0.06)
		self.send(key.scramble(key.startFreq))
		sleep(0.06)
		self.send(key.scramble(key.offset))
		sleep(0.06)
		
		order, count = key.getOrderAndCount(True)
		
		self.send(order)
		sleep(0.06)
		self.send(count)
		
	def addData(self, f, data, horizontal):
		for i, d in enumerate(data):
			if i % horizontal == 0 and i is not 0:
				f.write('\n')
			f.write(self.scramble(d) + ' ')
		
		
		
		
		
		
		
