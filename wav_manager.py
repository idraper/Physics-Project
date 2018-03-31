import numpy as np
from scipy.io import wavfile

class Wav_Manager():
	def __init__(self, fs=44100, s=44100, a=1000, t=10):
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
		print (self.y)
		
	def saveToFile(self, file='test.wav'):
		wavfile.write(file, self.Fs, self.y)
		
if __name__ == "__main__":
	w = Wav_Manager()
	w.newWave([1500, 1000, 3000])
	w.saveToFile()