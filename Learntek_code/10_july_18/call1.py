def fun1(list1):

	
	list1.append(67)
	print id(list1)
	print "Inside ", list1
	
list1 = [1,2,3,4]    # Call by reference means sending the memory address 
print " from Outside" ,list1   # Call by values means sending copy of value.
print id(list1)
fun1(list1)

print " from Outside after call" ,list1   # Call by values means sending copy of value.