list1 = [1,2,3,4,5,6,7,9,1,1,3,4]
d = {}
for each in list1:
	if each in d:
		d[each] = d[each]+1

	else :
		d.setdefault(each,1)
		
print (d)