import threading 
import time
lock = threading.Lock()
import datetime

t1 = datetime.datetime.now()


	
def second(n):
	lock.acquire()
	print (n)

def third():
	time.sleep(5)
	lock.release()
	print ("Thread3 ")


th1 = threading.Thread(target= second, args=("Thread1",))
th1.start()

th2 = threading.Thread(target= second, args=("Thread2",))
th2.start()

th3 = threading.Thread(target= third)
th3.start()

th1.join()
th2.join()
th3.join()

t2 = datetime.datetime.now()

print ("Total time", t2-t1)