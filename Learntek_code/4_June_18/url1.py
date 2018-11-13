import urllib
import re

ht =  urllib.urlopen('http://www.thapar.edu/faculties/category/departments/computer-science-engineering')

html_page = ht.read()

#mohitraj.cs@gmail.com
#pattern = re.compile(r'\b[\w.-]+@[\w.-]+\.\w+?\b')
pattern = re.compile(r'\b[\w.-]+@.+\.\w+')
for each in re.findall(pattern ,html_page):
	print each

