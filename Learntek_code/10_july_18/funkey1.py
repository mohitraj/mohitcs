def fun1(**var):
	print var
	for k,v in var.iteritems():
		print k, " : ", v

	
fun1(name = "Mohit", skill= "Python")