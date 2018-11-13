import re

string = "ab ihmhj abbbb   a"

p = "ab*"

m = re.search(p,string, flags= re.I)

if m :
	print m.group()
	print "start index", m.start()
	print "Last index ", m.end()
	print string[m.start():m.end()]