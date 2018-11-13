def fun4(list1):
	print "List in inside the function", list1
	list1.append(4)
	print "adding", list1
	print id(list1)
	
	
a = [1,2]
print id(a)
print "Outside the function", a
fun4(a)
print "Outside after fun call", a