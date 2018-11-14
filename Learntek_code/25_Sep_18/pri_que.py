import queue

Q1 = queue.PriorityQueue()  # Priority

#Q1.put(10)
#
list1 = [(2,"M"),(3,"A"),(4,"K")]

Q1.put((3, "Mohit"))
Q1.put((5, "Bhaskar"))
Q1.put((1, "Ravender"))
Q1.put((0, "Maninder Singh"))
Q1.put((10, "Nitin"))
print ("--------------------------------------------")

while not Q1.empty():
	print (Q1.get()[1])