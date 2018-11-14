list1 = [(1,3),(4,5),(3,0),(4,1),(4,2)]


def fun1(arg):   
	a,b = arg   # (1,3)
	return a+b 




list1.sort(key = fun1)  # keyworded argument 

print (list1)