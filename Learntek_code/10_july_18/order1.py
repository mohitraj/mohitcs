from collections import OrderedDict

d1 = OrderedDict()

d1[1] = "a"
d1[4] = 'd'
d1[3] = 'e'
d1[2] = 'b'

print "OrderedDict", d1


'''
def fun1(x):
	return x[1]
'''


d1 = OrderedDict(sorted(d1.items(), key=lambda x: x[1] ))

print d1