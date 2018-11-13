
try:
	num = int(raw_input("Enter the number \t"))
	a=  50/num
	
except ValueError:
	print "Please Enter the integer"
except ZeroDivisionError:
	print "Please don't use Zero"
	
except :
	print "New error"
else :
	print "From else", a
	