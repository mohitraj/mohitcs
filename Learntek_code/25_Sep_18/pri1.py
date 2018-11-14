import queue

Q1 = queue.PriorityQueue()  # Priority

#Q1.put(10)
#
list1 = [(2,"M"),(3,"A"),(0,"K")]

for each in list1:
	Q1.put(each)

while not Q1.empty():
	print (Q1.get()[1])