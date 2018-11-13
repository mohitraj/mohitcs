
def cmp1(x,y):
	
	if x==0 or y==0:
		c = y-x   #  dont swap
	else :
		c = x-y   # Swap
		
	return c
	
	
	
list2 = [10,9,3,7,2,0,23,0,561,0,0,96,0]

# [2, 3, 7, 9, 10, 23, 96, 561,1,1,1,1,1]

list2.sort(cmp=cmp1)

print list2