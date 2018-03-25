import sys, subprocess, wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft

#subprocess.call("ffmpeg -i Recording.m4a test.wav")

file = '440_sine.wav'

# open the wave file
fp = wave.open(file,"rb")
sample_rate = fp.getframerate()
total_num_samps = fp.getnframes()
#fft_length = int(sys.argv[2])
#num_fft = (total_num_samps / fft_length ) - 2

rate, data = wavfile.read(file)
fft_out = fft(data)

plt.plot(data, np.abs(fft_out))
plt.show()



sampFreq, snd = wavfile.read(file)
snd = snd / (2.**15)

dur = snd.shape[0] / sampFreq

print ("Duration: ", dur)

s1 = snd[:,0] 

timeArray = np.arange(0, snd.shape[0], 1)
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000  #scale to milliseconds

plt.plot(timeArray, s1, color='k')
plt.ylabel('Amplitude')
plt.xlabel('Time (ms)')
plt.show()