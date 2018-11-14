list1 = [1,2,8,9,0,4,0]
'''
list2 = []

for each in list1:
	if each!=0:
	
		a = each**2
		list2.append(a)
	else :
		print (each)
print (list2)
'''

print ([each**2 for each in list1  if each!=0])