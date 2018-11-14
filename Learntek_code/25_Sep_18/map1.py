#map(fun1, list1)

list1 = [0,1,4,37,100]

def fun1(temp):
	temp1 = 9/5*temp+32
	return temp1
	
m1 =  map(fun1,list1)

print (m1)
print (list(m1))