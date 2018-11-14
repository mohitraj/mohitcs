import threading
import time
def de():  # Normal 
	print ("Entering the daemon")
	time.sleep(3)
	print ("Exit the daemon")


def non_d():  # CEO type 
	print ("Entering the NON daemon")
	time.sleep(4)
	print ("Exit the NOn daemon")
	
	
th1 = threading.Thread(target= de)
th1.setDaemon(True)
th1.start()



th2 = threading.Thread(target=non_d)
th2.start()

# Head = main program