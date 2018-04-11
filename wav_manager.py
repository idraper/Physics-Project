import numpy as np
from scipy.io import wavfile

from key import Key

class Wav_Manager():
	def __init__(self, fs=128000, s=128000, a=100, t=10):
		self.A = a
		self.Fs = fs
		self.sample = s
		self.frequencies = None
		self.x = np.arange(self.sample*t)
		self.sum = np.zeros(self.sample*t)
		self.y = None

	def newWave(self, freq):
		self.frequencies = freq
		self.sumWaves(freq)
		
	def sumWaves(self, freq):
		for f in freq:
			self.sum = self.sum + np.sin(2 * np.pi * f * self.x/self.Fs)
		self.y = np.array(self.A * self.sum, dtype='int16')
		
	def saveToFile(self, file='test.wav'):
		wavfile.write(file, self.Fs, self.y)
		
	def getFile(self, file='test.wav'):
		return wavfile.read(file)