from collections import defaultdict

list_state = [('Newyork', "Hemested"), ('Newyork', 'NYC' ),('New_Jersi','Edison' ),('New_Jersi','Jersi_City'),('Texas', 'Dallas') ]

list_dict = defaultdict(list)
print (list_dict)

for k,v in list_state:
	print (k, ":", v)
	print (list_dict[k].append(v))
	
print (list_dict)