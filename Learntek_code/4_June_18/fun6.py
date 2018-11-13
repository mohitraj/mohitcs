k = 20

def fun6():
	global k
	k = k+9
	print k
	
	
def fun7():
	c = k+90
	print "From fun7 ", c
	
	
fun6()

fun7()

