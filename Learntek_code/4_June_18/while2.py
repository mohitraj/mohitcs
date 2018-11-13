import getpass



print "Hello World "

print "Please enter the password\t"
pass1 = getpass.getpass()

flag1 =0  
num =0
while True:
	if pass1=="India":
		
		print "Welcome in India"
		break

	else :
		print "Wrong password  type again"
		num = num+1
		print num
		if num==3:
			break
		print "Please enter the password again\t"
		pass1 = getpass.getpass()