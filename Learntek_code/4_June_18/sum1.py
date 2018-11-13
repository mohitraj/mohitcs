file_t = open("marks.txt",'r')

sum2= 0
i = 0
for each in file_t:
	each = each.strip("\n")
	each = float(each)
	sum2 = sum2+each
	i= i+1
print sum2
mean = sum2/i
print i, mean