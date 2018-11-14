import threading 

lock = threading.Lock()

def first(n):
	lock.acquire()
	a =12+n
	lock.release()
	print (a)
	
def second(n):
	lock.acquire()
	b = 12+n
	lock.release()
	print (b)

def all():
	lock.acquire()
	first(2)
	second(3)
	lock.release()
	
th1 = threading.Thread(target= all)
th1.start()

