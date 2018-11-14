list1 = ["titanium", "Learntek", "tigerwood"]

for str1 in list1:
	k = 0
	#print ("outer",str1)
	for i in str1:
		if i=="t":
			k = k+1
			
	print (str1, "t", "repeated ", k, "times")