from functools import reduce

list1 = [12,3,4,4,5,6]

def fun1(a,b):
	return a * b


a1 = reduce(fun1, list1)

print (a1)