# create a  square of numbers of lists
# if number is greater than 4

list1 = [1,2,3,4,6,5,9,10,12]
'''
list2 = []
for each in list1:
	if each >4:
		list2.append(each**2)
	
print list2
'''
#List comprehensions

print [each**2 for each in list1 if each> 4]