list1 = [4,5,0,6,6,13,0,4,0,20, 5,6,2,0,4,5,2]

m = max(list1)
def fun1(a):
	if a ==0 :
		return m+1
	else :
		return a
	



list1.sort(key= fun1)

print (list1)