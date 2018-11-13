import re

string = "1234&2445 b @#$%"

p = r'[^a-zA-Z0-9]'


p = re.compile(p)


a = re.sub(p,"", string)  #file = re.sub(r'[^a-zA-Z0-9]', '-', file)

print a 




'''

m = p.findall(string )   # findall(p, string)

if m :
	print "Occurred ", len(m), " times"
	
m1 = re.finditer(p,string)

for each in  m1:
	s = each.start()
	e = each.end()
	print "Starting index ", s, " Last index ", e
	
'''	
