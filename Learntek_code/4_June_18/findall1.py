import re

text = "In this world nothing is permanent "

p = re.compile("is")

for each in re.finditer(p,text):
	s = each.start()
	e = each.end()
	print "starting ",s , "Ending ",e
	

