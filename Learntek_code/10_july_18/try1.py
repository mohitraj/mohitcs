
try :
	
	a = float(raw_input("Enter the number\t "))
	c = 10/a
	
except Exception as e  :
	print e, type(e)


	

else :
	c = c +10
	print c 
	
finally:
	pass
	