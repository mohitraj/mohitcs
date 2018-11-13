#list1 = [4,5,6,6,13,4,5,6,2,4,5,2]

def fun1(tup1):
	return tup1[1]
	


list1 = [("a",30),("b",20),("c",10),("d",40),("e",45)]

list1.sort(key = fun1 )

print (list1)