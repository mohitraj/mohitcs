import math
# prime number program
#a = int(raw_input("Enter the number \t"))
list1 = [1,2,3,477,79,39]
# a =37    36  inter 37/2  18     sqrt(37)



for a in list1:
	s = int(round(math.sqrt(a)))+1
	flag =0
	for i in xrange(2,s):
		
		b=a%i
		if b==0:
			flag =1
			break
		
			
		
		
	if flag ==0:
		print "number  ",a," is prime " 
	else :
		print "Number is",a, " not prime "
	
