import  collections 

co1 = collections.Counter()
file_t = open("sample2.txt")

for line in file_t:
	line = line.lower()
	
	co1.update(line)


for k,v in  (co1.most_common(10)):
	print (k," repeated ", v, " times")
	