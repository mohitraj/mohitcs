import cPickle as p
file_r = open("port.txt","r")

dict1 = {}
for line in file_r:
	try:
		line = line.strip("\n")
		k,v = line.split(":",1)
		k = k.strip()
		dict1[k]=v
	except Exception as e :
		print e 
	
pickle_w = open("port.raj","w")

p.dump(dict1,pickle_w)

pickle_w.close()
	
file_r.close()