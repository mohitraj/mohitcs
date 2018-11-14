

# global scope 
# local scope 


def fun1(a):
	a = 80  # local variable 
	print ("Inside the function ",a)
	print ("inside the function ", id(a))
	return a
	
a = 30 # global variable 
print (fun1(a))
print ("Outside the function ", a , id(a))