list1 = [1,2,3,7,8,13,14,20,30,31]  # sorted n
list2 = [5,7,9,10,21,24,25]  # sorted   m

#merge it sorted
'''
list1.extend(list2)   #n+m  (10+10) 100

list1.sort()  # (n+m)

print (list1)
'''

len_list1 = len(list1)  # 8  , n  8

len_list2 = len(list2)  # 7  , m 4
list3 = []
n= 0
m = 0 
while n<len_list1 and  m <len_list2:      
	
	if list1[n] > list2[m] :   #  1 >5
		list3.append(list2[m])
		m = m+1
	else :
		list3.append(list1[n])
		n = n+1
		
if n==len_list1:
	list3.extend(list2[m:])
elif m== len_list2:
	list3.extend(list1[n:])
	
	
print (list3)
