port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}



print dict(zip(port1.values(),port1.keys()))

len1 = len(port1)
dict1 = {}
list1 = port1.keys()
list2 = port1.values()

for i in xrange(len1):
	dict1[ list2[i] ] = list1[i]
	
print dict1