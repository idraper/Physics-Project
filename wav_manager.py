import numpy as np
import pyaudio
from scipy.io import wavfile
import matplotlib.pyplot as plt
import scipy.fftpack

from key import Key
from wave_math import FastFFT

class Wav_Manager():
	def __init__(self, t=.1, fs=44100, s=44100, a=100):
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
		
		self.avg = None
		self.avgCheck = True
		

	def newWave(self, freq):
		self.frequencies = freq
		self.sumWaves(freq)
		
	def sumWaves(self, freq):
		for f in freq:
			self.sum = self.sum + np.sin(2 * np.pi * f * self.x/self.Fs)
			#plt.plot(np.sin(2 * np.pi * f * self.x/self.Fs)[:50])
		self.y = np.array(self.A * self.sum, dtype='int16')
		#plt.ylabel('Relative Amplitude')
		#plt.xlabel('Time (44100 Hz)')
		#plt.title('Plot of Individual Waves')
		#plt.plot(self.sum[:50])
		#plt.show()
		
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
		data = np.fromstring(self.stream.read(int(self.CHUNK/2)),dtype='int16')
		#data = np.fromstring(self.y,dtype='int16')
		#fft = FastFFT(data)
		fftData = np.fft.fft(data)
		norm = np.max(np.abs(fftData), axis=0)
		
		fft = np.asarray([np.sqrt(c.real ** 2 + c.imag ** 2)*(1/norm) for c in fftData][:int(len(data)/2)])
		
		plt.pause(.00001)
		plt.gcf().clear()
		x = np.fft.fftfreq(1024, d = 1.0 / (2*self.RATE))
		x = np.linspace(0, self.RATE, len(data))
		#plt.plot(x[:int(len(x)/2)], [np.sqrt(c.real ** 2 + c.imag ** 2)*(1/self.RATE) for c in fft.calcFreqs()][:int(len(data)/2)])
		#plt.ylabel('Relative Amplitude')
		#plt.xlabel('Frequencies')
		#plt.title('Frequency Plot')
		#plt.plot(x[:int(len(x)/2)], fft)
		plt.draw()
		
		if self.avgCheck:
			self.avg = np.zeros(len(fft))
			self.avg = fft
			self.avgCheck = False
			
		self.avg = (self.avg + fft) / 2
		plt.plot(x[:int(len(x)/2)], self.avg)
		
		#print (x)
		#i = [x*10 for x, c in enumerate(fftData[:int(len(fftData)/2)]) if np.sqrt(c.real ** 2 + c.imag ** 2)*(1/norm) > .6]
		i = [x*100 for x, c in enumerate(self.avg) if c > .6]
		
		return i
		
	def startAudio(self):
		self.p = pyaudio.PyAudio() # start the PyAudio class
	def endAudio(self):
		self.p.terminate()
		
	def startStream(self):
		self.stream = self.p.open(format=pyaudio.paInt16,channels=1,rate=self.RATE,input=True, \
			frames_per_buffer=int(self.CHUNK/2)) #uses default input device
	def endStream(self):
		self.stream.stop_stream()
		self.stream.close()
		
	
		
		
