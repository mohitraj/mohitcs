import Queue

q1 = Queue.PriorityQueue()  # FIFO Queue

q1.put((1,"Mohit "))
q1.put((15,"Manish"))
q1.put((10,"Bhaskar"))

q1.put((0,"Root"))

while not q1.empty():
	print q1.get()[1]
