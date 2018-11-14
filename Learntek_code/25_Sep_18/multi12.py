from multiprocessing import Process, Manager
import time
import random

mgr = Manager()


list1 = mgr.list()

def Producer1():  # Normal 
	print ("inth1",id(list1))
	while True:
	
		a = random.randint(1,100)
		list1.append(a)
		time.sleep(.5)
	


def Consumer1():  # CEO type 
	print ("inth2",id(list1))
	time.sleep(4)
	while True:
		
		
		print (list1.pop())
		
	
	
th1 = Process(target= Producer1)

th1.start()



th2 = Process(target=Consumer1)
th2.start()
