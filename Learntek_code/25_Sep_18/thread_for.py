import threading 
import time
list1 = []
class MyThread(threading.Thread):
	def __init__(self,i):
		threading.Thread.__init__(self)
		self.h = i
		
	def run(self):
		time.sleep(3)
		list1.append(self.h)
		print ("Value added ", self.h)
		
list2 = []	
for each in range(5):
	thread1 = MyThread(each)
	list2.append(thread1)
	thread1.start()
	
	
for thread in list2:
	thread1.join()


print ("All work done",list1)