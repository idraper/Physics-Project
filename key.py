import numpy as np

class Key():
	def __init__(self, m='', f='encryption', sF=5000, sO=250):
		self.data = m.lower()
		self.size = len(self.data)
		self.startFreq = sF
		self.offset = sO
		self.keyVal = 0
		for num, char in enumerate(f):
			self.keyVal += ord(char) * num
		self.keyVal %= 75
		
		self.lexData = None
		self.order = None
		self.count = None
		
		
	def set(self, num, s, oF, oR, cnt):
		self.size = num
		self.lexData = d
		self.offset = oF
		self.startFreq = s
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
		
	def decodeMessage(self, freq, fromFile=True):
		if fromFile:
			num, start, offset, order, count = self.readFile()
			out = np.zeros(num, dtype='str')
			
			m = self.freqToLexo(freq, start, offset)
			
			oPos = 0 	# points to order
			cPos = 0 	# points to count
			
			for char in m:
				while count[cPos] > 0:
					out[order[oPos]] = char
					oPos += 1
					count[cPos] -= 1
				cPos += 1
			
			return ''.join(str(x) for x in out)
		else:
			out = np.zeros(self.num, dtype='str')
			m = self.freqToLexo(freq, self.start, self.offset)
			
			for char in m:
				while self.count[cPos] > 0:
					out[self.order[oPos]] = char
					oPos += 1
					self.count[cPos] -= 1
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
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
