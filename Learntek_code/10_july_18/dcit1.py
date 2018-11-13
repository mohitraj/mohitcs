Port = {22: "SSH", 80: "HTTP", 443 : "HTTPS", 3306 : "MYSQL"  }

list1 = [21,22, 20,25,80,90,443]

'''
for each in list1:
	if each in Port:
		print each, " : ", Port[each]
	else :
		print "Value for ", each , " not in database"
'''
'''
for each in list1:
	print Port.get(each,"Not present")
	
'''

for each in list1:
	if Port.has_key(each):
		print Port[each]
	else :
		print "Value not present"