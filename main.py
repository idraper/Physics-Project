import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from key import Key
from wav_manager import Wav_Manager
from networking import MySocket as Socket
from wave_math import Math

if __name__ == "__main__":
	k = Key("new test message")
	print ('Original:\n', k.getMessage())
	k.saveToFile()
	print ()
	#print ('Decoded from file:\n', k.decodeMessage(k.getFrequencies(), True))
	print ()
	#print (sorted(k.getFrequencies()))
	
	w = Wav_Manager()
	w.newWave(k.getFrequencies())
	w.saveToFile()
	#w.play()
	#w.startAudio()
	#w.startStream()
	'''
	try:
		while True:
			w.listen()
	except KeyboardInterrupt:
		pass
	'''
	
	conn = Socket()
	mode = input('Mode: ')
	if mode == 's':
		print ('sending data')
		conn.connect('192.168.1.133', 8000)
		conn.sendKey(k)
		conn.close()
	else:
		print ('recieving data')
		num, start, offset, order, count = conn.recieve('192.168.1.133', 8000)
		k = Key("")
		k.set(num, start, offset, order, count)
		print ('Decoded from real time:\n', k.decodeMessage([32500, 33750, 29250, 34000, 30750, 13000, 30250, 34750, 32250]))
		
	'''
	plt.plot(w.getFile()[1][:150])
	plt.show()
	
	plt.hist(sorted(k.getFrequencies())[:-4], 500)
	plt.xlabel('frequencies')
	plt.show()
	'''