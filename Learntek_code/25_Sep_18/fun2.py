def even1(list1):
	list2 = []
	for each in list1:
		c = each%2
		if c ==0:
			list2.append(each)
		
	return  (list2)
	
print (even1([1,2,3,4,5,6]))
print (even1( [10,20,3,4,5,78]))
print (even1([6,7,83,56,34,90]))