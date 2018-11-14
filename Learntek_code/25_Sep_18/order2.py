import collections
d1 = {'a':1, "x": 4, "y":78, "d": 10, "e": 11, "f": 2}

def fun1(tup1):
	return tup1[1]

#d2 = collections.OrderedDict()
#d2=  collections.OrderedDict((sorted(list(d1.items()), key= fun1)))

list1 = list(d1.items()) # tuple pair list


d2=  collections.OrderedDict((sorted(list1, key= lambda tup1: tup1[1])))

print (d2)