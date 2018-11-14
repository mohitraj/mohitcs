import threading
import time
import random


list1 = []

def Producer1():  # Normal 
	while True:
		a = random.randint(1,100)
		list1.append(a)
		time.sleep(1)
	


def Consumer1():  # CEO type 
	while True:
		print (list1.pop())
		time.sleep(1)
	
	
th1 = threading.Thread(target= Producer1)

th1.start()



th2 = threading.Thread(target=Consumer1)
th2.start()