
try:
	num = int(raw_input("Enter the number \t"))
	a=  50/num
	
except (ValueError,ZeroDivisionError):
	print "Either you pressed 0 or string"

	
else :
	print "From else", a
	
finally:
	print "FInally program ends here "
	