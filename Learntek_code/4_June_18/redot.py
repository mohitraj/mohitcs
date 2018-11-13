import re
line = "5a3f2B56"
#pattern = r"^Ev"

#pattern = r'a.?b'

pattern = r'[^5]'

print re.findall(pattern ,line,flags= re.MULTILINE)


for each in re.finditer(pattern ,line,flags= re.MULTILINE):
	s = each.start()
	e = each.end()
	print "starting ",s , "Ending ",e