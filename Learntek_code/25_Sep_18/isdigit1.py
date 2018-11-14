utilization = ["10", "34","a", "12" ]
bandwidth = 100
for each in utilization:
	if each.isdigit():
		a1 = int(each)/bandwidth
		print (a1)