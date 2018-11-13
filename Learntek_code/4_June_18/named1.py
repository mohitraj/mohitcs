import collections

employee = collections.namedtuple('Mohit','name age empid',rename=True)

list1 = ['Shankar',28,23456 ]


record1 = employee._make(list1)

print "Before updation", record1
record1= record1._replace(age= 25)

print "After updation", record1


