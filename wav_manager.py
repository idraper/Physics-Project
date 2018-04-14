import numpy as np
import pyaudio
from scipy.io import wavfile
import matplotlib.pyplot as plt
import scipy.fftpack

from key import Key

class Wav_Manager():
	def __init__(self, fs=44100, s=44100, a=100, t=.1):
		self.A = a
		self.Fs = fs
		self.sample = s
		self.frequencies = None
		self.x = np.arange(int(self.sample*t))
		self.sum = np.zeros(int(self.sample*t))
		self.y = None
		
		self.CHUNK = 4096 # number of data points to read at a time
		self.RATE = 44100 # time resolution of the recording device (Hz)
		self.p = None
		self.stream = None
		

	def newWave(self, freq):
		self.frequencies = freq
		self.sumWaves(freq)
		
	def sumWaves(self, freq):
		for f in freq:
			self.sum = self.sum + np.sin(2 * np.pi * f * self.x/self.Fs)
		self.y = np.array(self.A * self.sum, dtype='int16')
		
	def saveToFile(self, file='test.wav'):
		wavfile.write(file, self.Fs, self.y)
		print("* Wrote audio file!")
		
	def getFile(self, file='test.wav'):
		return wavfile.read(file)
		
	def play(self):
		print("* Generating sample...")
		tone_out = np.array(self.y, dtype='int16')
		bytestream = tone_out.tobytes()
		pya = pyaudio.PyAudio()
		stream = pya.open(format=pya.get_format_from_width(width=1), channels=1, rate=self.Fs, output=True)
		try:
			print ("* Previewing audio... Press 'Ctrl + c' to stop playback")
			while True:
				stream.write(bytestream)
		except KeyboardInterrupt:
			pass
		stream.stop_stream()
		stream.close()

		pya.terminate()
		print("* Preview completed!")
		
	def listen(self):
		
		data = np.fromstring(self.stream.read(self.CHUNK),dtype='int16')
		
		plt.pause(.00001)
		plt.gcf().clear()
		plt.plot(scipy.fftpack.fft(data)[:500])
		plt.draw()
		return data
		
	def startAudio(self):
		self.p = pyaudio.PyAudio() # start the PyAudio class
	def endAudio(self):
		self.p.terminate()
		
	def startStream(self):
		self.stream = self.p.open(format=pyaudio.paInt16,channels=1,rate=self.RATE,input=True, \
			frames_per_buffer=self.CHUNK) #uses default input device
	def endStream(self):
		self.stream.stop_stream()
		self.stream.close()
		
	
		
		
