import os
print os.getcwd()
os.chdir("K:/Learntek/Slides/test")
print os.getcwd()

'''

for each in os.listdir('.'):
	name_list = each.rsplit(".",1)
	ext1 = name_list[1]
	name = name_list[0]
	if ext1.isupper():
		ext1 = ext1.lower()
		new_name = name+"."+ext1
		os.rename(each,new_name)
		
'''
		
for each in os.listdir('.'):
	name_list = each.rsplit(".",1)
	ext1 = name_list[1]
	name = name_list[0]
	if ext1.lower()!='png':
		os.remove(each)
		
	
		

