import random
list1 = [1,2,3,4,5,6,7,8,9,0]
list2= ['a','b','c','d','e','f']


list3 = random.sample([each.upper() for each in list2],1)+random.sample(list1,5)+ random.sample(list2,3)

print "".join([str(each) for each in list3])