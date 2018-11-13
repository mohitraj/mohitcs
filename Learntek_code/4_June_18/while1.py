print "Hello World "

pass1 = raw_input("Please enter the password\t")

flag1 =0  
num =0
while flag1==0:
	if pass1=="India":
		
		print "Welcome in India"
		flag1 =1

	else :
		print "Wrong password  type again"
		num = num+1
		print num
		if num==2:
			flag1= 1
		pass1 = raw_input("Please enter the password again\t")
		

	