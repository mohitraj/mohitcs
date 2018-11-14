def fun1(b,c= 10,*a):   # fun1(10)
	print (b)
	print (c)
	print (a)
	print (type(a))
	sum1 =1
	for each in a:
		sum1 = sum1+each
	return  (sum1)
	



print (fun1(10,20,56,45,23))




