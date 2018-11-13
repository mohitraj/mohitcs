from threading import *
import time

class mythread(Thread):
	def __init__(self,i):
		Thread.__init__(self)
		self.h = i

		
	def run(self):
		print "Values is ", self.h
		#time.sleep(1)
		

thread1 = mythread(1)
thread1.setDaemon(True)
thread1.start()



thread2 = mythread(2)
thread2.start()

print thread1.isDaemon()

print thread2.isDaemon()
