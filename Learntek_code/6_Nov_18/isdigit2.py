list1 = ['1',"",'3','4','5']



for each in list1:
	if each.isdigit():
		each = int(each)
		c = 100/each
		print(c) 	