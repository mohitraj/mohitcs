import re

p1 = "wit+h" 
text = "Peace begin wittth with smile "

m2 = re.finditer(p1, text)
print (m2)

for m1 in m2:

	print (m1.group())
	print ("start at ",m1.start())
	print ("Ends at ", m1.end())
	
