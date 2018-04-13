import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from key import Key
from wav_manager import Wav_Manager
from networking import MySocket as Socket

if __name__ == "__main__":
	k = Key("new test message")
	print ('Original:\n', k.getMessage())
	k.saveToFile()
	print ()
	print ('Decoded from file:\n', k.decodeMessage(k.getFrequencies()))
	print ()
	#print (sorted(k.getFrequencies()))
	
	w = Wav_Manager()
	w.newWave(k.getFrequencies())
	w.saveToFile()
	#w.play()
	w.startAudio()
	w.startStream()
	
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
		print (conn.recieve('192.168.1.133', 8000))
	'''
	
	'''
	plt.plot(w.getFile()[1][:150])
	plt.show()
	
	plt.hist(sorted(k.getFrequencies())[:-4], 500)
	plt.xlabel('frequencies')
	plt.show()
	'''