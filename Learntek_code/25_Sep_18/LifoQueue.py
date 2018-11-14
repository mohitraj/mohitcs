import queue

Q1 = queue.LifoQueue()  # LIFO

#Q1.put(10)

for each in [12,3,5,'a',3.4]:
	print (each)
	Q1.put(each)
print ("--------------------------------------------")

while not Q1.empty():
	print (Q1.get())