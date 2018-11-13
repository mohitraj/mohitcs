import re
import urllib

url = "http://www.thapar.edu/faculties/category/departments/computer-science-engineering"

html = urllib.urlopen(url)

text=html.read()

#print text

email  = r'[\w.-]+@[\w.-]+\.[a-zA-Z]+'

#\w = [a-zA-Z0-9_]    hello.mail.com
#email = "abcA_b.ab@gmail.com"
#()hj@hj.cm
		
		

email = re.compile(email)

for each in set(re.findall(email, text)):
	print each

	
