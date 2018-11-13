import collections

txt = raw_input("Enter the txt \t")

file_r = open("sample2.txt",'r') 


co1 = collections.Counter()

for line in file_r:
	#line = line.strip("\n")
	line = line.split()
	co1.update(line)

print co1[txt]