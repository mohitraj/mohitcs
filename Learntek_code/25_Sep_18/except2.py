def sum1(a,b):
	try:
		c = a+b
		return c 
	except Exception as e :
		print (e )
	
def divide(a,b):
	try:
		c = a/b
		print (c)
	except Exception as e :
		pass

	
def sub(a,b):
	c = a-b
	return c 
	
	

#print (sum1(12,34))

divide(3,0)
print (sub(10,5))