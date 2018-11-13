a = 10  # global value 

def fun1():
	global a
	a = a+ 90  # local value
	c = 20 +a 
	print a
	
	
	
fun1()

print "outside ", a 

