import numpy as np

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
			
			
			
			
			
			
			
			
			
