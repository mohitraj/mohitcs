
port1 = {22: 'SSH', 23: 'Telnet', 20: 'FTP', 53: 'DNS', (12, 45): 'Combine', 81: 'Unknow port', 'Python': 'programming language'}
key1 = int(input("Enter the key\t"))

if key1 in port1:
	print ("Key already exists")

