import threading

lock = threading.RLock()
def fun1(n):
	
	lock.acquire()
	
	lock.acquire()
	print ("Inside the function")
	print (n)
	lock.release()
	lock.release()

thread1 = threading.Thread(target= fun1, args = (20,) )
thread1.start()


thread2 = threading.Thread(target= fun1, args = (10,) )
thread2.start()