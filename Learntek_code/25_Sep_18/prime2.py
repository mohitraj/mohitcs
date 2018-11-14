num1 = int(input("ENter the number : "))

#adult method
flag = 1

num2 = int(num1/2)


for each in range(2,num2):
	c = num1%each
	if c==0:
		flag =0
		print ("divisible by", each )
		break
		
if flag==1:
	print ("Number is prime ")
else :
	print ("Number is not prime")