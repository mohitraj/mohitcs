import threading 
import time

class MyThread(threading.Thread):
	def __init__(self,i):
		threading.Thread.__init__(self)
		self.h = i
		
	def run(self):
		print ("Value added ", self.h)
		time.sleep(1)
	
thread1 = MyThread(10)
thread1.start()

thread2 = MyThread(20)
thread2.start()

print ("Total number of threads", threading.activeCount())	
print ("List", threading.enumerate())