import re

p1 = "wit+h" 
text = "Peace begin wittth witth smile "

m1=re.sub(p1, 'with', text,1 )

print (m1)
