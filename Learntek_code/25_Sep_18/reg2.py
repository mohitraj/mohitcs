import re

p1 = r'[^a-zA-Z0-9# ]'
 
text = "Peace @###$% \xbegin wi^$E#%ttth witth@#$% smile "

m1=re.sub(p1, '', text )

print (m1)