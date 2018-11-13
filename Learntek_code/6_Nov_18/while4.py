sum1 = 0
flag = 0

while flag==0 :
	num1 = int(input("Enter the number to add, press 0 to exit: "))
	if num1 ==0 :
		flag = 1
	sum1 = sum1 + num1 
	print (sum1)
	
print ("Final sum is %d"%(sum1))