import re
import urllib

url = "http://www.thapar.edu/faculties/category/departments/computer-science-engineering"

html = urllib.urlopen(url)

text=html.read()

p1 = r'\b[\w.-]+?@\w+?\.\w+?\b'  #34h-u.lk_123@marvel.com

p1 = re.compile(p1)


m1 = re.findall(p1, text)


for email in m1:
	print (email)