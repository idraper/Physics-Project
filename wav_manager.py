import numpy as np
from scipy.io import wavfile

Fs = 44100
f1 = 1000
f2 = 700
sample = 44100
x = np.arange(sample*10)

w1 = np.sin(2 * np.pi * f1 * x/Fs)
w2 = np.sin(2 * np.pi * f2 * x/Fs)
s_waves = [w1, w2]

sum = np.zeros(sample*10)

for w in s_waves:
	sum = sum + w

y = np.array(1000 * sum, dtype='int16')
print (y)

wavfile.write('test.wav', Fs, y)