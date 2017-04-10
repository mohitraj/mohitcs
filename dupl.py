#program created by mohit
#offical website L4wisdom.com
# email-id  mohitraj.cs@gmail.com
import os
import re
import sys
from threading import  Thread
from datetime import datetime
import subprocess
import cPickle
import argparse
import hashlib
import collections

dict1 = collections.defaultdict(list)

def md5(fname,size=4096):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(size), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def all_duplicate(file_dict):
	
	file_txt = open('duplicate.txt', 'w')
	all_file_list = [v for k,v in file_dict.items()]
	for each in all_file_list:
		if len(each)>2:
			file_txt.write("-------------------\n")
			for i in each:
				str1 = i+"\n"
				file_txt.write(str1)
	file_txt.close()

def get_drives():
	response = os.popen("wmic logicaldisk get caption")
	list1 = []
	total_file = []
	t1= datetime.now()
	for line in response.readlines():
		line = line.strip("\n")
		line = line.strip("\r")
		line = line.strip(" ")
		if (line == "Caption" or
					line == ""):
			continue
		list1.append(line)
	return list1
	
def search1(drive,size):
	for root, dir, files in os.walk(drive, topdown = True):
		try:
			for file in files:
				try:
					if os.access(root, os.X_OK):
						orig = file
						file = root+"/"+file
						if  os.access(file, os.F_OK):
							if os.access(file, os.R_OK):
								s1=md5(file,size)
								dict1[s1].append(file)
	
				except Exception as e :
					pass
		except Exception as e :
			pass
				
def create(size): 
	t1= datetime.now()
	list2 = []   # empty list is created	
	list1 = get_drives()
	print "Drives are \n"
	for d in list1:
		print d," " ,
	print "\nCreating Index..."			
	for each in list1:
		process1 = Thread(target=search1, args=(each,size))
		process1.start()
		list2.append(process1)
		  
	for t in list2:
		t.join() # Terminate the threads

	print len(dict1)
	pickle_file = open("mohit.dup1","w") 
	cPickle.dump(dict1,pickle_file) 
	pickle_file.close()
	t2= datetime.now()
	total =t2-t1
	print "Time taken to create " , total
	
	
def file_open():
	pickle_file  = open("mohit.dup1", "r")
	file_dict = cPickle.load(pickle_file)  
	pickle_file.close()
	return file_dict

	
def file_search(file_name):
	t1= datetime.now()
	try:
		file_dict  = file_open()
	except IOError:
		create()
		file_dict  = file_open()
	except Exception as e :
		print e 
		sys.exit()
	file_name1 = file_name.rsplit("\\",1)
	os.chdir(file_name1[0])

	file_to_be_searched = file_name1[1]
	if  os.access(file_name, os.F_OK):
		if os.access(file_name, os.R_OK):
			sign = md5(file_to_be_searched)
			files=  file_dict.get(sign, None)
			if files:
				print "File(s) are "
				files.sort()
				for index, item in enumerate(files):
					print index+1," ", item
					print "---------------------"
	else :
		print "File is not present or accessible"
	t2= datetime.now()
	total =t2-t1
	print "Time taken to search " , total

def main():
	parser = argparse.ArgumentParser(version='1.0')
	parser.add_argument("file_name",nargs='?', help="Give file with path in double quotes")
	
	parser.add_argument('-c',nargs='?', help="For creating MD5 hash of all files",const=4096, type=int)
	parser.add_argument('-a',help="To get all duplicate files in duplicate.txt in running current folder", action='store_true')
	parser.add_argument('-f',help="To find the MD5 hash,provide file with path in double quotes ", nargs=1,)
	
	args = parser.parse_args()	
	try:
		if args.c:
			print args.c
			create(args.c)	
			
		elif args.a :
			file_dict  = file_open()
			all_duplicate(file_dict)
			
		elif args.f :
			if os.access(args.f[0], os.R_OK):
				print "Md5 Signature are : ", md5(args.f[0],4096)
				print "\n"
			else :
				print "Check the file path and file name\n"
		else:
			file_search(args.file_name)
		print "Thanks for using L4wisdom.com"
		print "Email id mohitraj.cs@gmail.com"
		print "URL: http://l4wisdom.com/finder_go.php"
		
	except Exception as e:
		print e
		print "Please use proper format to search a file use following instructions"
		print "dupl file-name"
		print "Use <dupl -h >  For help"
main()

