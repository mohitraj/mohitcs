# for loop with the strings
j=0
k=0
for i in "abscfdgswsdsdoscsdssssss":
	#print i
	k=k+1
	if 's'==i:
		j=j+1
		if j==5:
			break
	
print "S  occurred", j, "TImes"