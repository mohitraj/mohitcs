from multiprocessing import Process
import time


def non_d():  # CEO type 
	print ("Entering the NON daemon")
	time.sleep(4)
	print ("Exit the NOn daemon")
	
	




th2 = Process(target=non_d)
th2.start()

#th2.join(5)

#print ("Thread is live ?", th2.isAlive())




print ("All done ")