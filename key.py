import numpy as np

class Key():
	def __init__(self, me='', f='encryption', sF=500, sO=100):
		self.data = me.lower()
		self.size = len(self.data)
		self.startFreq = sF
		self.offset = sO
		self.keyVal = 0
		for num, char in enumerate(f):
			self.keyVal += ord(char) * num
		self.keyVal %= 75
		
		self.order = None
		self.count = None
		
		
	def set(self, num, s, oF, oR, cnt):
		self.size = self.unscrambleInt(int(num, 0))
		self.offset = self.unscrambleInt(int(oF, 0))
		self.startFreq = self.unscrambleInt(int(s, 0))
		self.order = oR
		self.count = cnt
		
		
	def newMessage(self, m):
		self.data = m
		
	def getMessage(self):
		return self.data
	
	def getMessageList(self):
		return list(set(self.data))
		
	def getMessageListFull(self):
		return list(self.data)
		
	def getMessageLexoFull(self):
		return sorted(list(self.data))
		
	def getMessageLexo(self):
		return sorted(list(set(self.data)))
		
	def saveToFile(self, fN='key.txt'):
		f = open(fN, 'w')
		f.write(self.scramble(len(self.getMessageListFull())))
		f.write(' ')
		f.write(self.scramble(self.startFreq))
		f.write(' ')
		f.write(self.scramble(self.offset))
		f.write('\n')
		
		order, count = self.getOrderAndCount()
		
		self.addData(f, order, 10)
		f.write('\n')
		f.write('\n')
		self.addData(f, count, 10)
		f.write('\n')
		f.write('\n')
		
	def getOrderAndCount(self, scram=False):
		order = []
		count = []
		for i, d in enumerate(self.getMessageLexo()):
			c = 0
			for j, char in enumerate(self.getMessageListFull()):
				if d == char:
					if scram:
						order.append(self.scramble(j))
					else:
						order.append(j)
					c += 1
			if scram:
				count.append(self.scramble(c))
			else:
				count.append(c)
		return (order, count)
			
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
		order = []
		count = []
		
		num, start, offset = stuff[0].replace('\n', '').split()
		
		num = self.unscrambleInt(num)
		start = self.unscrambleInt(start)
		offset = self.unscrambleInt(offset)
		
		stuff.pop(0)
		tmp = []
		while stuff[0] != '\n':
			tmp.append([self.unscrambleInt(x) for x in stuff[0].split()])
			stuff.pop(0)
		for x in tmp:
			order += x
		stuff.pop(0)
		
		tmp = []
		while stuff[0] != '\n':
			tmp.append([self.unscrambleInt(x) for x in stuff[0].split()])
			stuff.pop(0)
		for x in tmp:
			count += x
			
		return (num, start, offset, order, count)
		
	def decodeMessage(self, freq, fromFile=False):
		oPos = 0 	# points to order
		cPos = 0 	# points to count
		if fromFile:
			num, start, offset, order, count = self.readFile()
			out = np.zeros(num , dtype='str')
			
			m = self.freqToLexo(freq, start, offset)
			
			for char in m:
				while count[cPos] > 0:
					out[order[oPos]] = char
					oPos += 1
					count[cPos] -= 1
				cPos += 1
			
			return ''.join(str(x) for x in out)
		else:
			self.order = self.order[2:-2]
			self.count = self.count[2:-2]
			order = [self.unscrambleInt(x) for x in list(self.order.split("', '"))]
			count = [self.unscrambleInt(x) for x in list(self.count.split("', '"))]
			out = np.zeros(self.size, dtype='str')
			m = self.freqToLexo(freq, self.startFreq, self.offset)
			for char in m:
				while count[cPos] > 0:
					out[order[oPos]] = char
					oPos += 1
					count[cPos] -= 1
				cPos += 1
			
			return ''.join(str(x) for x in out)
			
	def unscrambleInt(self, num):
		try:
			return num - self.keyVal
		except:
			return int(num, 0) - self.keyVal
	
	def unscramble(self, num):
		return chr(num - self.keyVal)
		
	def getFrequencies(self):
		#return [self.startFreq + (x*self.offset) for x in range(len(self.getMessageList()))]
		return [self.startFreq + (ord(x)*self.offset) for x in self.getMessageList()]
		
	def freqToLexo(self, freq, start, offset):
		return sorted([chr(int((x-start)/offset)) for x in freq])
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
