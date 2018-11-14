import  collections 

co1 = collections.Counter()

co1.update("learntek python programming")

for each in "aeoui":
	print (each, " : ", co1[each])
