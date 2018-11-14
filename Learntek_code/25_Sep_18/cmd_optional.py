import argparse
list1 = [1,2,3,4,5,6]

def rev():
	return list1[::-1]







parser = argparse.ArgumentParser() 

parser.add_argument("-R", help= "Print reverse of the list", action= 'store_true')
parser.add_argument("-Pi", help= "A constant number ", action= "store_const", const= 3.14)

arg = parser.parse_args()
print (arg)
if arg.R:
	print (rev())
	
if arg.Pi:
	print (arg.Pi)