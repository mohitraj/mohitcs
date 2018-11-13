sum1 = 0
while True :
	num1 = int(input("Enter the number to add, press 0 to exit: "))
	if num1 ==0 :
		break
	sum1 = sum1 + num1 
	print (sum1)
	
print ("Final sum is %d"%(sum1))