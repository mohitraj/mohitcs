#1 . NUmber range 1-100

#2 number can be repeated 
import random
list1 = []
a = "1"
while True:
	r=  random.randint(1,100)
	
	
	if a =='0':
		break
	if r not in list1:
		print r
		list1.append(r)
		a = raw_input("Press Enter button press 0 to end")
		