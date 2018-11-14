def fun1(list1):
	print ("inside the function",list1)
	list1.append(10)
	print ("inside the function", id(list1)  )
	print ("inside the function", list1)
	
list2 = [5,6,7]

fun1(list2)

print ("outside the function", list2, id(list2))

