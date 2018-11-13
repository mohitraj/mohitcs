import Queue

q1 = Queue.LifoQueue()  # FIFO Queue


for i in xrange(5):
	print "Insertion", i
	q1.put(i)
	
while not q1.empty():
	print q1.get()


