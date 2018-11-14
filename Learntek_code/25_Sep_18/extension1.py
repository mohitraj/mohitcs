import os

os.chdir("K:/Learntek/25_Sep/test")

print (os.getcwd())

for file in  os.listdir("."):
	if file.endswith('png'):
		file_name, ext =file.rsplit(".",1)
		new_name = file_name+"."+"PNG"
		os.rename(file,new_name)