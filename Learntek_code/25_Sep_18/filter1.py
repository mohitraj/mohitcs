#filter(fun1, list1)
import sys


list1 = [1,2,3,4,56,89,0,34,23,2,4,5,2,2,6,8,10]

def fun1(a):
	c = a%2 
	if c ==0:
		return False 
	else :
		return True

a1 =  (filter(fun1, list1))

print (list(a1))

print (sys.getsizeof(a1))
