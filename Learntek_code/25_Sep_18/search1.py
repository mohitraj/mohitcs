import re

p1 = "wit+h" 
text = "Peace begin wittth with smile "

m1 = re.search(p1, text)

if m1:
	print (m1.group())
	print ("start at ",m1.start())
	print ("Ends at ", m1.end())