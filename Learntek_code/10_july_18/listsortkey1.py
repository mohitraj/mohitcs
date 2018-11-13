#list.sort(cmp=None, key=None, reverse=False)

list1 = [("a",4,14),("b",1,13),("v",5,12),("f",2,15)]

def fun1(x):
	return x[2]
	
list1.sort(key=fun1)

print list1
	
	
	
