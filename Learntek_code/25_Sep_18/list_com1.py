list1 = [1,21,31,1,41,5,101,0,0,4,1,5,6,0,0,1,4,5]  #[21,4,4,5,5....... 0, 0,0,0,0]



def fun1(a,b): #1,21,31,41,5,0,0,4,5,6,0,0,4,5
	c = a-b
	if a ==0 or b==0:
		return 1
	else :
		return c 
	
	
	
	
	
list1.sort(cmp=fun1)

print (list1)
