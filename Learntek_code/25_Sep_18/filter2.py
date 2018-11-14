#filter(fun1, list1)
import sys


list1 = [1,2,3,4,56,89,0,34,23,2,4,5,2,2,6,8,10]

	

a1 =  (filter(lambda a :a%2, list1))

print (list(a1))

print (sys.getsizeof(a1))