#threading.Timer(interval, function, args=[], kwargs={})

import threading 

def fun1(a,b):
	print ("Hello everyone",a,b)

threading.Timer(10, fun1, args=["M","K"],).start()