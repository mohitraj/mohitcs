import re 
pattern = "this" 
text = " in this world nothing is permanent this is last number this" 
for match in re.findall(pattern,text): 
   print "found", match

for match in re.finditer(pattern,text): 
   print match
   s = match.start() 
   e = match.end() 
   print "Found", match.re.pattern, s, "from", e 
   
print re.finditer(pattern,text)