import os

dict1 = {}
i= 0
for each in os.walk("K:/Learntek/skill", topdown=True, onerror=None, followlinks=False):
	root, dir, files = each
	for file in files:
		if dict1.has_key(file):
			i = i+1
			file = file +"|"+str(i)
		dict1[file] = root
	


for k,v in dict1.iteritems():
	if "|" in k:
		k = k.split("|",1)[0]
	
	print k, " : ", v