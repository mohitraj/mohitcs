import configparser 
import time
import shutil
import hashlib
from distutils.dir_util import copy_tree
from collections import OrderedDict
import os
import logger1 as log1
import argparse
def ConfRead(file=None):
	if file:
		file_name = file
	else :
		file_name = "Sync1.ini"
	config = configparser.ConfigParser()
	config.read(file_name)
	return (dict(config.items("Para")))

def md5(fname,size=4096):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(size), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
	

def CopyDir(from1, to):
	copy_tree(from1, to)
	
def CopyFiles(file, path_to_copy):
	shutil.copy(file,path_to_copy)

def OriginalFiles(All_Config):
	drive = All_Config.get("from")
	Files_Dict = OrderedDict()
	print (drive)
	for root, dir, files in os.walk(drive, topdown=True):
			for file in files:
				if not file.startswith("~$"):
					file = file.lower()
					file_path = root+'\\'+file
					try:
						hash1 = md5(file_path,size=4096)
						#modification_time = int(os.path.getmtime(file_path))
						rel_path = file_path.strip(drive)
						Files_Dict[(hash1,rel_path)]= file_path
					except Exception as e :
						log1.logger.error('Error Original files: {0}'.format(e))
						
	return Files_Dict
	
	
def Destination(All_Config):
	Files_Dict = OrderedDict()
	from1 = All_Config.get("from")
	to= All_Config.get("to")
	dir1= from1.rsplit("\\",1)[1]
	drive = to+dir1
	#print (drive)
	try:
		if os.path.isdir(drive):
			for root, dir, files in os.walk(drive, topdown=True):
					for file in files:
						
						file = file.lower()
						file_path = root+'\\'+file
						try:
							hash1 = md5(file_path,size=4096)
							#modification_time = int(os.path.getmtime(file_path))
							rel_path = file_path.strip(drive)
							Files_Dict[(hash1,rel_path)]= file_path
						except Exception as e :
							log1.logger.error('Error Destination foor loop: {0}'.format(e))
			return Files_Dict
		else :
			CopyDir(from1,drive)
			log1.logger.info('Full folder: {0} copied'.format(from1))
			return None
	except Exception as e :
		log1.logger.error('Error Destination: {0}'.format(e))
	
def LogicCompare(All_Config):
	from1 = All_Config.get("from")
	to= All_Config.get("to")
	Dest_dict = Destination(All_Config)
	if Dest_dict:
		Source_dict = OriginalFiles(All_Config)
		remaining_files = set(Source_dict.keys())- set(Dest_dict.keys())
		remaining_files= [Source_dict.get(k) for k in remaining_files]
		
		for file_path in remaining_files:
			try:
				log1.logger.info('File: {0}'.format(file_path))
				dir, file = file_path.rsplit("\\",1)
				rel_dir = from1.rsplit("\\",1)[1]
				rel_dir1 = dir.replace(from1,"")
				dest_dir = to+rel_dir+"\\"+rel_dir1
				if not os.path.isdir(dest_dir):
					os.makedirs(dest_dir)
				CopyFiles(file_path, dest_dir)
			except Exception as e :
				log1.logger.error('Error LogicCompare: {0}'.format(e))
				

def run(repeat,Freq,All_Config):				
	i = 0			
	while True:
		if i >= repeat:
			break
		LogicCompare(All_Config)
		time.sleep(Freq)
		i = i +1
		
		
def main():
	version1 = 3.0
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', help="Version Number", action='store_true')
	parser.add_argument('-f', nargs=1, help='Give SYNC file name')
	args = parser.parse_args()
	if args.v :
		print ("Version -> ",version1)
		return 0
	elif args.f:
		All_Config =  ConfRead(args.f[0])
	else :
		All_Config =  ConfRead()
	

	Freq = int(All_Config.get("freq"))*60 
	Total_time = int(All_Config.get("total_time"))*60
	repeat = int(Total_time/Freq)
	run(repeat,Freq,All_Config)
	
if __name__ == "__main__":
	main()
				