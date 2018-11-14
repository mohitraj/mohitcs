import re

p1 = "with" 
text = "Peace begin with smile "

m1 = re.match(p1, text)

if m1:
	print (m1.group())