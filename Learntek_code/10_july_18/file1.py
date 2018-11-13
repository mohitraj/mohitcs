file_txt = open("sample1.txt", 'r')


i = 0
for line in file_txt:
	print line
	if 'is' in line:
		i = i+1
		
print i


file_txt.close()
