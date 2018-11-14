import queue
import threading

q1 = queue.Queue()

def fun1():
	while True:
		print (q1.get())
		q1.task_done()
	
	

	
thread1 = threading.Thread(target=fun1)
thread1.setDaemon(True)
thread1.start()

for each in range(5):
	q1.put(each)


q1.join()

