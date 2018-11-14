list1 = [1,21,31,1,41,5,101,0,0,4,1,5,6,0,0,1,4,5]  #[21,4,4,5,5....... 0, 0,0,0,0]

max1 = max(list1)

def fun1(a): #1,21,31,41,5,0,0,4,5,6,0,0,4,5
	if a==1:
		return max1+1
	else :
		return a 
	
	
list1.sort(key=fun1)

print (list1)
