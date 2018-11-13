import random
list1 = [1,2,3,4,5,6,7,'a','b','c','d']

list2 =  random.sample(list1,6)

list2 = [str(each) for each in list2]

print "".join(list2)




