

try:
	num1 = int(input("Enter the number "))
	result = 10/num1
	print (result)
	
except ValueError:
	print ("use integer")
	
except ZeroDivisionError:
	print ("Don't use zero")
	
except :
	print ("Unknow error")
	
else :
	d1 = result+1

	print ("d1",d1)