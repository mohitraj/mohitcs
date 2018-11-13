list1 = [12,34,None,45,30]
bandwidth = 100
for each in list1:
	if each == None :
		continue
	kpi = each/bandwidth*100
	print (kpi)
	