import collections

list1 = [1,2,3,4,5]

de = collections.deque(list1)

print (de)

de.rotate(-2)
print ("\n")
print (de)

print (dir(de))