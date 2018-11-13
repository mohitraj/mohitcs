from threading import Timer 

def fun1(str1):
	print "HEllo ", str1
	
str1 = "mohit"

Timer(4, fun1, (str1,)).start()