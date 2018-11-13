import os
import logger1 as lg
dict1 = {}
i= 0
for each in os.walk("K:/Learntek/skill", topdown=True, onerror=None, followlinks=False):
	root, dir, files = each
	for file in files:
		try:
			if dict1.has_key(file):

				i = i+1
				file = file +"|"+str(i)
				raise IOError
			lg.logger.info(file)
			dict1[file] = root
		except Exception as e :
			lg.logger.error('Error in t: {0} {1}'.format(i,e))
	


for k,v in dict1.iteritems():
	if "|" in k:
		k = k.split("|",1)[0]
	
	print k, " : ", v