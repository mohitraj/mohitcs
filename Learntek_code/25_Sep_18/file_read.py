file_t  = open("sample1.txt", 'r')  # File type object 

for each in file_t:
	if "mohit" in each:
		print (each)
	
	
	
	
file_t.close()