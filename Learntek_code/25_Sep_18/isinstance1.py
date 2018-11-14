#isinstance()

list1 = [23,'67',None,78,None,56,23,""]
bandwidth = 81

for each in list1:
		if isinstance(each, int) or isinstance(each, float):
			kpi = round((each/bandwidth)*100,2)
			print (kpi)
		else :
			#print (each)
			pass