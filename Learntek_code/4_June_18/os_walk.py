import os
top = 'K:/Learntek/class'
for each in  os.walk(top, topdown=False, onerror=None, followlinks=False):
	root, dirs, files = each
	print "Root dir ", root
	print "Directories ", dirs
	print "files are ", files
	
	
	
