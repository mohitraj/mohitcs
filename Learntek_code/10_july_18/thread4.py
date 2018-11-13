from threading import Thread
from time import sleep

def sum(a):   #GUI
	
	print "Entering in SUM"
	sleep(1)
	print a
	print "finish the SUM"
	
	
	
	
def multi(a):   # executed by Daemon thread
	
	print "Entering in multi"
	sleep(3)
	
	print "Finish the multi"
	
	
	
	
thread1 = Thread(target=sum, args=(1,))
thread1.start()

thread2 = Thread(target=multi, args=(2,))
thread2.setDaemon(True)
thread2.start()

thread1.join()
thread2.join()