#list.sort(cmp=None, key=None, reverse=False)

def cmp1(a,b):
	if a==0 or b==0:
		c = b-a
	else :
		c = a-b  #10   9 
	return c    # A positive number , negative number or Zero  for +ve I we have descending order -ve we have ascending order 
		

list1 = [10,9,3,7,2,0,23,0,561,0,0,96,0]  #  list1 = [(10,9),(9,3),(3,7),(7,2)......]

list1.sort(cmp=cmp1)

zero_index=  list1.index(0)

print list1[:zero_index]

