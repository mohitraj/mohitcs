import threading
import time
import random
import queue


Q1= queue.Queue()

def Producer1():  # Normal 
	while True:
		a = random.randint(1,100)
		Q1.put(a)
		#time.sleep(1)
	


def Consumer1():  # CEO type 
	while True:
		print (Q1.get())
		time.sleep(1)
	
	
th1 = threading.Thread(target= Producer1)

th1.start()



th2 = threading.Thread(target=Consumer1)
th2.start()