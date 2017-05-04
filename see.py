import os
import re
import sys
import argparse

class Text_search :
	def __init__(self, string2, path1,i=None):
		self.path1= path1
		self.string1 = string2
		self.i=i
		if self.i:
			string2 = string2.lower()
		self.string2= re.compile(string2)
	def txt_search(self):
		file_number = 0
		files = [f for f in os.listdir(self.path1) if os.path.isfile(self.path1+"/"+f)]
		for file in files:
			file_t = open(self.path1+"/"+file)
			file_text= file_t.read()
			if self.i:
				file_text=file_text.lower()
			file_t.close()
			if re.search(self.string2, file_text):
				print "The text "+self.string1+" found in ", file
				file_number=file_number+1
		print "total files are ",file_number
			
	def txt_search_m(self):
		files = [f for f in os.listdir(self.path1) if os.path.isfile(self.path1+"/"+f)]
		file_number = 0
		for file in files:
			file_t = open(self.path1+"/"+file)
			line_number=1
			flag_file = 0
			for line1 in file_t:
				if self.i:
					line1 = line1.lower()
				if re.search(self.string2, line1):
					flag_file= 1
					print "The text "+self.string1+" found in ", file, " at line number ",line_number
				line_number=line_number+1
			if flag_file == 1:
				file_number=file_number+1
				flag_file=0
			file_t.close()	
		print "total files are ",file_number
	
	def txt_search_r(self):
		file_number = 0
		for root, dir, files in os.walk(self.path1, topdown = True):
			files = [f for f in files if os.path.isfile(root+"/"+f)]
			for file in files:
				file= root+"/"+file
				file_t = open(file)
				line_number=1
				flag_file = 0
				for line1 in file_t:
					if self.i:
						line1=line1.lower()
						
					if re.search(self.string2, line1):
						flag_file= 1
					
						print "The text "+self.string1+" found in ", file, " at line number ",line_number
						line_number=line_number+1
				if flag_file == 1:
					file_number=file_number+1
					flag_file=0
				file_t.close()	
			
		print "total files are ",file_number
				
def main():
	parser = argparse.ArgumentParser(version='2.0')
	parser.add_argument('-m', nargs = 2, help = 'To get files as well as line number of files ')
	parser.add_argument('-s', nargs = 2, help = 'To get the files contain string ')
	parser.add_argument('-r', nargs = 2, help = 'To search in recusrive order ')
	parser.add_argument('-mi', nargs = 2, help = '-m option with case insensitive ')
	parser.add_argument('-si', nargs = 2, help = '-s option with case insensitive ')
	parser.add_argument('-ri', nargs = 2, help = '-r option with case insensitive ')
	
	args = parser.parse_args()	
	
	try:
		if args.m:
			dir = args.m[1]
			obj1 = Text_search(args.m[0],dir)
			obj1.txt_search_m()
				
		elif args.s:
		
			if args.s[1]:
				dir = args.s[1]
				obj1 = Text_search(args.s[0],dir)
				obj1.txt_search()
					
		elif args.r:
			if args.r[1]:
				dir = args.r[1]
				obj1 = Text_search(args.r[0],dir)
				obj1.txt_search_r()

		elif args.mi:
			dir = args.mi[1]
			obj1 = Text_search(args.mi[0],dir,i=1)
			obj1.txt_search_m()
				
		elif args.si:
		
			if args.si[1]:
				dir = args.si[1]
				obj1 = Text_search(args.si[0],dir,i=1)
				obj1.txt_search()
					
		elif args.ri:
			if args.ri[1]:
				dir = args.ri[1]
				obj1 = Text_search(args.ri[0],dir,i=1)
				obj1.txt_search_r()
				
		
		print "\nThanks for using L4wisdom.com"
		print "Email id mohitraj.cs@gmail.com"
		print "URL: http://l4wisdom.com/see_go.php"
		
	except Exception as e:
		print e
		print "Please use proper format to search a file use following instructions"
		print "see file-name"
		print "Use <see -h >  For help"
main()

