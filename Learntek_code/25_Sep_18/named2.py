#from collections import namedtuple
import collections

emp1 =collections.namedtuple("Learntek", 'name age empid', rename= False ) # creating own data type

list1 = ['shankar',28, 123456]


record1 = emp1._make(list1)


print (record1)

print (record1.name)

print (record1.age)
print (record1.empid)