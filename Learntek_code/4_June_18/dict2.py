list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c","d","e"]

len1= max(len(list1),len(list2))

#print dict(zip(list1,list2))

print dict([(list1[i],list2[i])  for i in xrange(len1)])


