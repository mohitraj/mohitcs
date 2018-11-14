import argparse
list1 = [1,2,3,4,5,6]

parser = argparse.ArgumentParser() 

parser.add_argument("-T", nargs=2, help= "Hours" )
parser.add_argument("-H", nargs="?", help= "One arguments")
parser.add_argument("-M",nargs= "*", help = "0 to many")
parser.add_argument("-S", nargs= '+', help= "1 to many")

arg = parser.parse_args()

if arg.T:
	print (arg.T)
	print (arg.T[0])
if arg.H:
	print (arg.H)
	
if arg.M:
	print (arg.M)
if arg.S:
	print (arg.S)