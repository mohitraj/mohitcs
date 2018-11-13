list1 = [1,2,3,4,5,6,7,67,34,12]
'''
def fun1(a):
	t = a%2
	if t ==1:
		return 0 
	else :
		return 1
'''

	
	
final_list = filter(lambda a:  a%2,list1)
print final_list
