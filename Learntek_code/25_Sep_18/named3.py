#from collections import namedtuple
import collections

emp1 =collections.namedtuple("Learntek", 'name age empid', rename= False ) # creating own data type

record1 = emp1('shankar',28, 123456) 

print (record1)

print (record1.name)

print (record1.age)

record1=  record1._replace(age=25)

print (record1.age)


print (record1.empid)
print (record1)