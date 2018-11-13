def fun2(a):
	print " before Inside", id(a)
	a = a + 5
	print "Inside", id(a)
	print "Inside the function", a
	
a = 10

fun2(10)	
print "Outside ", a 
print "outside", id(a)