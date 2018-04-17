import numpy as np
import sys, math
sys.setrecursionlimit(3000)

class Math():
	def __init__(self, amps, sfs):
		self.amplitudes = amps
		self.N = len(self.amplitudes)
		self.sample_frequency = sfs
		self.nyquist_limit = self.sample_frequency / 2
		self.calc_parts()
		self.calc_mag()
		self.calc_freq()
		
		self.real_part = []
		self.imag_part = []
		self.mags = []
		self.freqs = []
		
	def calc_parts(self):	
		tmp = 0.0
		for k in range(self.N):
			for n in range(self.N):
				tmp += self.amplitudes[n] * np.cos((2 * np.PI * k * n)/ self.N)
			self.real_part.push_back(tmp)
			tmp = 0.0
			
		for k in range(self.N):
			for n in range(self.N):
				tmp += self.amplitudes[n] * np.sin((2 * np.PI * k * n)/ self.N)
			self.imag_part.push_back(tmp)
			tmp = 0.0
			
		for i in range(self.N):
			print ("Re[f(", i, ")] : ", self.real_part[i], "\t\tIm[f(", i,")] : ", self.imag_part[i])
			
		return
		
	def calc_mag(self):
		tmp = 0.0
		for i in range(self.N):
			tmp = np.sqrt(np.pow(self.real_part[i], 2) + np.pow(self.imag_part[i], 2))
			self.mags.push_back(tmp)
			
		for i in range(self.N):
			print ("Magnitudes: ", i, self.mags[i])
			
		return
		
	def calc_freq(self):
		tmp = 0.0
		for i in range(self.N - self.nyquist_limit):
			tmp = (self.mags[i] * 2) / self.N
			self.freqs.push_back(tmp)
			
		return
			
			
class FastFFT():
	def __init__(self, a, sR=44100, useW=True):
		self.RATE = sR
		self.nyquist_limit = self.RATE / 2
		self.amps = a
		self.N = len(self.amps)
		self.c_amps_r = []
		self.c_amps_c = []
		self.freqs = []
		
		if (useW):
			print ("Applying Hann Window")
			self.applyHanningWindow()
			
		if (not self.isPowOfTwo(self.N)):
			print ("Zero padding vector ", self.N)
			self.zeroPad()
			print ("...Done zero padding.")
			
		self.frame_size = self.N / self.RATE
		
		print ("Starting bit reversal")
		print (self.N)
		self.bitReverseVector(self.amps, self.N)
		print ("... Bit reversal done.")
		
		print ("Initializing complex vector...")
		self.c_amps_r = self.amps
		for i in range(len(self.c_amps_r)):
			self.c_amps_c.append(0)
		print ("Initialization done...")
		
		print ("Calculating FFT...")
		self.calcFFT()
		print ("...FFT analysis done.")
		print ("Processing frequencies...")
		self.calcFreqs();
		print ("...Done")
	
	def isPowOfTwo(self, val):
		compare = 1
		
		while (compare < val):
			compare = int(compare) << 1
		if val == compare:
			return True
		return False
	
	def makePowOfTwo(self, val):
		compare = 1
		if val > compare:
			while val > compare:
				compare = int(compare) << 1
				#print (val, compare)
		elif val < compare:
			compare = 1
		return compare
	
	def zeroPad(self):
		oldN = self.N
		self.N = self.makePowOfTwo(self.N)
		for i in range(self.N - oldN):
			self.amps = np.append(self.amps, 0)
		
	def applyHanningWindow(self):
		k = 2 * np.pi / (self.N - 1)
		tmp = np.arange(len(self.amps))
		self.amps = self.amps * (1.0/2.0 * (1.0 - np.cos(k * tmp)))
		return
		
	def bitReverseVector(self, vToReverse, size):
		even = []
		odd = []
		
		if size == 2:
			return
			
			
		for i in range(0, len(vToReverse), 2):
			even.append(vToReverse[i])
		for i in range(1, len(vToReverse), 2):
			odd.append(vToReverse[i])
			
		self.bitReverseVector(even, len(even))
		self.bitReverseVector(odd, len(odd))
		
		for i in range(int(size/2)):
			vToReverse[int(size/2) + i] = odd[i]
		return
	
	def calcFFT(self):
		even_c = 0.0
		even_r = 0.0
		odd_c = 0.0
		odd_r = 0.0
		odd_x_t_c = 0.0
		odd_x_t_r = 0.0
		tmp_c = 0.0
		tmp_r = 0.0
		
		WN = np.pi * 2 / self.N
		log2N = np.log2(self.N)
		
		WnK_tbl_c = []
		WnK_tbl_r = []
		for k in range(self.N + 1):
			WnK_tbl_c.append(tmp_c)
			WnK_tbl_r.append(tmp_r)
			WnK_tbl_r[k] = np.cos(WN * k)
			WnK_tbl_c[k] = np.sin(WN * k)
			
		stride = 1
		while stride < self.N:
			stage = np.log2(self.N / stride)
			#print ("Stage: ", stage)
			k = 0
			while k < self.N:
				n = 0
				for n in range(stride):	
					i1 = k + n
					i2 = k + n + stride
					WnK_i = ((n * stride) % self.N)
					
					even_r = self.c_amps_r[i1]
					even_c = self.c_amps_c[i1]
					odd_r = self.c_amps_r[i2]
					odd_c = self.c_amps_c[i2]
					odd_x_t_r = WnK_tbl_r[WnK_i] * odd_r + WnK_tbl_c[WnK_i] * odd_c
					odd_x_t_c = WnK_tbl_c[WnK_i] * odd_r + WnK_tbl_r[WnK_i] * odd_c
					
					self.c_amps_r[i1] = even_r + odd_x_t_r
					self.c_amps_c[i1] = even_r + odd_x_t_c
					self.c_amps_r[i2] = even_r - odd_x_t_r
					self.c_amps_c[i2] = even_c + odd_x_t_c
				k += (stride << 1)		
			stride = stride << 1
		return
		
	def calcFreqs(self):
		tmp_v = 0.0
		tmp_m = 0.0
		for i in range(len(self.c_amps_c)):
			tmp_v = i / self.frame_size
			tmp_m = math.sqrt(self.c_amps_r[i]**2 + self.c_amps_c[i]**2)
			tmp_m = (tmp_m * 2) / self.N
			self.freqs.append(tmp_m)
		return self.freqs
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
