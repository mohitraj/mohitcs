
list1 = [1,2,3,4,5,6,6,'9',8,7,0,'hjj','ert',8,8]


for each in list1:
	try:
		c = 50/int(each)
		print c
	except Exception as e:
		print e 
		print each


