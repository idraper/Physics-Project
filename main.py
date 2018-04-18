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
	print ('Decoded from file:\n', k.decodeMessage(k.getFrequencies(), True))
	print ()
	print (sorted(k.getFrequencies()))
	
	w = Wav_Manager(60)
	w.newWave(k.getFrequencies())
	w.saveToFile()
	#w.play()
	w.startAudio()
	w.startStream()
	
	'''
	order = "['"
	for x in k.getOrderAndCount()[0]:
		order += str(x) + "', '"
	order = order[:-4]
	order += "\']"
	
	count = "['"
	for x in k.getOrderAndCount()[1]:
		count += str(x) + "', '"
	count = count[:-4]
	count += "\']"
	'''
	
	
	
	conn = Socket()
	mode = input('Mode: ')
	if mode == 's':
		print ('sending data')
		conn.connect('10.24.196.104', 8000)
		conn.sendKey(k)
		conn.close()
	else:
		print ('recieving data')
		num, start, offset, order, count = conn.recieve('10.24.196.104', 8000)
		k = Key("")
		k.set(num, start, offset, order, count)
		print ('Decoded from real time:\n', k.decodeMessage([32500, 33750, 29250, 34000, 30750, 13000, 30250, 34750, 32250]))
		
	try:
		while True:
			data = w.listen()
			decode = Key()
			decode.set(k.getStart(), k.getOff(), order, count)
			print (data)
			print ('Decoded (real):\n', decode.decodeMessage(data))
	except KeyboardInterrupt:
		pass
		
	'''
	plt.plot(w.getFile()[1][:300])
	plt.title('Wave Plot')
	plt.ylabel('Sum of Sine-Waves')
	plt.xlabel('Time (44100 Hz)')
	plt.show()
	'''
	
	
	
	
	
	
	
	
	
	
	
