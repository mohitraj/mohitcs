import threading 
list1 = [(1,2,3),(4,5,6),(7,8,9)]

for a,b,c in list1:
	#a,b,c = each  # unpacking
	print (a,b,c)
	
print (threading.activeCount())