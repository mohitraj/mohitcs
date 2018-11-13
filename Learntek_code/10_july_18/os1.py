import os
os.chdir('K:/Learntek/Slides/test')
for file1 in  os.listdir('.'):
	if file1.endswith("jpg"):
		file = file1.rsplit(".",1)[0]
		new_name = file+"."+'png'
		os.rename(file1,new_name)
		



