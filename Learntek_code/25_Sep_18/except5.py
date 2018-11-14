try:
	num1 = int(input("Enter the number "))
	result = 10/num1
	print (result)
	
	
	
except (ValueError,ZeroDivisionError):
	print ("Int or 0 error")
	

	
except :
	print ("Unknow error")