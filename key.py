import numpy as np

class Key():
	def __init__(self, m='', f='encryption'):
		self.data = m
		self.size = len(self.data)
		
		self.keyVal = 0
		for num, char in enumerate(f):
			self.keyVal += ord(char) * num
		self.keyVal %= 75
		
	def newMessage(self, m):
		self.data = m
		
	def getMessage(self):
		return self.data
	
	def getMessageList(self):
		return list(set(self.data))
		
	def getMessageLexo(self):
		return sorted(list(set(self.data)))
		
	def saveToFile(self, fN='key.txt'):
		f = open(fN, 'w')
		f.write(self.scramble(len(self.getMessageList())))
		f.write('\n')
		f.write('\n')
		self.addData(f, self.getMessageList(), 10)
		f.write('\n')
		f.write('\n')
		
	def addData(self, f, data, horizontal):
		for i, d in enumerate(data):
			if i % horizontal == 0 and i is not 0:
				f.write('\n')
			f.write(self.scramble(d) + ' ')
		
	def scramble(self, d):
		if type(d) is str:
			val = ord(d)
		elif type(d) is int:
			val = d
		else:
			val = 0
		return str(hex(val + self.keyVal))
		
	def readFile(self, fN='key.txt'):
		f = open(fN, 'r')
		stuff = list(f)
		stuff.pop()
		print (self.unscrambleInt(int(stuff[0].replace('\n', ''), 16)))
		stuff.pop(0)
		stuff.pop(0)
		print (stuff)
		for line in stuff:
			line = line.replace('\n', '')
			for d in line.split():
				print (self.unscramble(int(d, 0)))
				
	def unscrambleInt(self, num):
		return num - self.keyVal
	
	def unscramble(self, num):
		return chr(num - self.keyVal)
		
if __name__ == '__main__':
	key = Key()