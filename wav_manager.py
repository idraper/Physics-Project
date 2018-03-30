import numpy as np
from scipy.io import wavfile

class Wav_Manager():
	def __init__(self, fs=44100, freq=[440], s=44100, a=1000, t=10):
		
		self.A = a
		self.Fs = fs
		self.sample = 44100
		self.frequencies = freq
		self.x = np.arange(self.sample*t)
		
		self.sum = np.zeros(self.sample*t)

		for f in self.frequencies:
			self.sum = self.sum + np.sin(2 * np.pi * f * self.x/self.Fs)

		self.y = np.array(self.A * self.sum, dtype='int16')

		wavfile.write('test.wav', self.Fs, self.y)
		
if __name__ == "__main__":
	w = Wav_Manager()