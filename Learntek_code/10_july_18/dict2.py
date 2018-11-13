Port = {22: "SSH", 80: "HTTP", 443 : "HTTPS", 3306 : "MYSQL"  }
'''
for each in Port.items(): #[(80, 'HTTP'), (3306, 'MYSQL'), (443, 'HTTPS'), (22, 'SSH')]
	k,v =  each #  unpacking   k,v = (80, 'HTTP')
	print k , " : ", v 
	
'''
#1000000  50 MB
#Port.items()  50 MB
'''
for k,v in Port.iteritems(): #[(80, 'HTTP'), (3306, 'MYSQL'), (443, 'HTTPS'), (22, 'SSH')]
	#k,v =  each #  unpacking   k,v = (80, 'HTTP')
	print k , " : ", v 
	
'''

for each in Port.iterkeys():
	print each