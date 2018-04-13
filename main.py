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
		conn.connect('192.168.1.133', 80)
		conn.send('test')
	else:
		conn.connect('192.168.1.126', 80)
		print(conn.recieve())
	
	
	'''
	plt.plot(w.getFile()[1][:150])
	plt.show()
	
	plt.hist(sorted(k.getFrequencies())[:-4], 500)
	plt.xlabel('frequencies')
	plt.show()
	'''