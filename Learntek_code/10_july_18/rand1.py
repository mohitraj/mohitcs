import random
list1 = []
while True:
	flag = 0 
	a = random.randint(1,100)
	if a not in list1:
		list1.append(a)
		print a
		flag = 1
		
	if flag ==1:
		raw_input("Press enter to get the number ")
	
