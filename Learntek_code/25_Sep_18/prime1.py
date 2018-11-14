num1 = int(input("ENter the number : "))

#kid method
flag = 1




for each in range(2,num1):
	c = num1%each
	if c==0:
		flag =0
		print ("divisible by", each )
		break
		
if flag==1:
	print ("Number is prime ")
else :
	print ("Number is not prime")