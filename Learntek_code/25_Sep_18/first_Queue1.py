import queue

Q1 = queue.Queue()  # FIFO

Q1.put(10)

print (Q1.get())
print (Q1.get())