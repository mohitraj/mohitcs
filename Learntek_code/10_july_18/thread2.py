from threading import *
import time

lock = RLock()

class mythread(Thread):
	def __init__(self,i):
		Thread.__init__(self)
		self.h = i
		
	def run(self):
		lock.acquire()   
		time.sleep(1)
		print "Values is ", self.h
		lock.acquire() 
		
		lock.release()
		lock.release()
		
		
		
list1 = []
for i in xrange(5):
	thread1 = mythread(i)
	thread1.start()
	list1.append(thread1)
	
for each in list1:
	each.join()


print "\nGood bye \n"

