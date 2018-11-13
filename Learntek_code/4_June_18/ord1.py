from  collections import OrderedDict

def fun1(tup1):
	x,y= tup1
	return y

ord_dict1 = OrderedDict()

ord_dict1['M'] = 3
ord_dict1['O'] = 2
ord_dict1['H'] = 1
ord_dict1['I'] = 6
ord_dict1['T'] = 7

#print "Order dict ", ord_dict1

print ord_dict1.items()

dict1=sorted(ord_dict1.items(),key=fun1)

print OrderedDict(dict1)

