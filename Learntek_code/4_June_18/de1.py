from  collections import defaultdict

list_state = [('Haryana', 'Yamunanagar'), ('Haryana', 'Ambala'), ('Haryana', 'karnal'), ('Punjab', 'patiala'), ('Punjab', 'Chandigarh'), ('UP', 'Noida')] 
	
	
d2 = dict(list_state)
print d2

d1 = defaultdict(list)


for each in list_state:
	k,v = each   # ('Haryana', 'Yamunanagar')
	d1[k].append(v)
	
print d1
	


