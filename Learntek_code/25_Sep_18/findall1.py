import re

p1 = "wit+h" 
text = "Peace begin wittth with smile "

m1 = re.findall(p1, text)
print (m1)
print ("Total number of occurrence ", len(m1))
'''
if m1:
	print (m1.group())
	print ("start at ",m1.start())
	print ("Ends at ", m1.end())
	
'''