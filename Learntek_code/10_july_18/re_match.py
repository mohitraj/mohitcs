import re

string = "What we think we become"

p = "what"

m = re.search(p,string, flags= re.I)

if m :
	print m.group()