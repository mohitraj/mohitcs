import os
import re
import sys
from threading import  Thread
from datetime import datetime
import subprocess



if len(sys.argv)>1 and len(sys.argv)<4 :

	response = os.popen("wmic logicaldisk get caption")
	list1 = []
	
	total_file = []
	t1= datetime.now()
	for line in response.readlines():
		line = line.strip("\n")
		line = line.strip("\r")
		line = line.strip(" ")
		if (line == "Caption" or line == ""):
			continue
		list1.append(line)
	a = "\\"
	def search1(drive):
		total = 0
		global total_file
		for root, dir, files in os.walk(drive, topdown = True):
			for file in dir:
				if sys.argv[1] == '-i':
					if re.search(sys.argv[2].lower(), file.lower()):
						file=  root+a+file
						print file
						total_file.append(file)
					#total = total+1 
				
				elif re.search(sys.argv[1], file):
					file=  root+a+file
					print file
					total_file.append(file)
					#total = total+1 
		#print "Total File(s) in\t", drive, "are ", total
		#print "\nthank for using l4wisdom.com\n"

	list2 = []   # empty list is created	

				
	for each in list1:
		process1 = Thread(target=search1, args=(each,))
		process1.start()
		list2.append(process1)
	  
	  
	for t in list2:
		t.join() # Terminate the threads
	subprocess.call('cls',shell=True)
	total_file.sort(key=lambda x: x.split(":")[0])
	for file in total_file:
		print file
	print "Total File(s) are\t", len(total_file)
	print  "\nThanks for using l4wisdom.com\n" 
	t2= datetime.now()
	total =t2-t1
	print "Searching completed in " , total

else :
	print "Wrong foramte, please use formate as shown below:"
	print "locate <file-name>"
	print "for case insensitive use :"
	print "locate -i <file-name>"



