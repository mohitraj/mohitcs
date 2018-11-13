import os
from collections import defaultdict

dict1 = defaultdict(list)
i= 0
for each in os.walk("K:/Learntek/skill", topdown=True, onerror=None, followlinks=False):
	root, dir, files = each
	for file in files:
		dict1[file].append(root)
	


for k,v in dict1.iteritems():
	
	
	print k, " : ", v