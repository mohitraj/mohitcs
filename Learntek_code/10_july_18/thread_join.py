from threading import Thread
from time import sleep

def sum(a):   #GUI
	
	print "Entering in SUM"
	sleep(2)
	print a
	print "finish the SUM"
	
def multi(a):   
	
	print "Entering in multi"
	sleep(5)
	
	print "Finish the multi"

thread1 = Thread(target=sum, args=(1,))
thread1.start()
thread1.join(3)
thread2 = Thread(target=multi, args=(2,))

thread2.start()
thread2.join(3)

print "Thread1",thread1.isAlive()
print "Thread2",thread2.isAlive()

print "Good bye"