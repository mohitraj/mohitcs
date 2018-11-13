from collections import Counter

file_t = open("sample2.txt", 'r')

co1  =  Counter()

for line in file_t:
	line = line.strip("\n")
	line = line.replace( " ", "")
	co1.update(line.lower())
	
print co1

print "\n"
for x,y in co1.most_common(5):
	print x , "  : " , y