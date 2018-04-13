import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from key import Key
from wav_manager import Wav_Manager
from networking import MySocket as Socket
#from networking import Host as host
#from networking import Client as client

if __name__ == "__main__":	
	'''
	k = Key("new message")
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
	#w.listen()
	'''
	
	conn = Socket()
	mode = input()
	if mode == 's':
		print ('sending data')
		conn.connect('192.168.1.133', 8000)
		conn.send('test')
	else:
		print ('recieving data')
		conn.recieve('192.168.1.133', 8000)
	
	
	'''
	plt.plot(w.getFile()[1][:150])
	plt.show()
	
	plt.hist(sorted(k.getFrequencies())[:-4], 500)
	plt.xlabel('frequencies')
	plt.show()
	'''