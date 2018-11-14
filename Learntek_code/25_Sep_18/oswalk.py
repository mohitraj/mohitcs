import os


h1=os.walk("K:/Learntek/25_Sep/test", topdown=False, onerror=None, followlinks=False)

for root, dirs, files in h1:
	print ("Root is : ", root)
	print ("Folder are : ",dirs)
	print ("Files are : ", files)
	print ("******************************************")
	