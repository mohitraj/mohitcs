dict1 = {}

try:
	file_t = open("sample1.txt", 'r')


	for line in file_t:
		#print line 
		line = line.strip("\n")
		if dict1.get(line,None):
			print line 
		else :
			dict1[line]= "jkll"

	
	
	file_t.close()
except Exception as e :
	print e 