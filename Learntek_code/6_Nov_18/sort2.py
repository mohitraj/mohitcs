#list1 = [4,5,6,6,13,4,5,6,2,4,5,2]

def fun1(tup1):
	return tup1[1]+tup1[0]
	


list1 = [(10,30,40),(10,20),(30,10),(2,40),(0,45)]

list1.sort(key = fun1 )

print (list1)