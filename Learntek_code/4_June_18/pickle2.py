import cPickle as p

port_number = [80,22,99,67,53,22,443,445,135,0]

pickle_r = open("port.raj","r")

data = p.load(pickle_r )
#print data
for p in port_number:
	p = str(p)
	print p, " \t ", data.get(p,"Not found ")



