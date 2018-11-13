import re
line = "Every thing is planned"
pattern = "thing"

m = re.search(pattern , line, flags = re.I )
if m:
	print m.group()
	print "Starting point", m.start(), "End point", m.end()
	
else :
	print "Not found"