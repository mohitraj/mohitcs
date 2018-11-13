from threading import *
import time

class mythread(Thread):
	def __init__(self,i):
		Thread.__init__(self)
		self.h = i
		print "Current thread is ",currentThread()
		
	def run(self):
		#print "Values is ", self.h
		time.sleep(1)
		
print "Active threads before", activeCount() 
thread1 = mythread(1)
thread1.start()

thread2 = mythread(2)
thread2.start()
print "Active threads After", activeCount()
print "Current thread is ",currentThread()
print "Active threads are ", enumerate()