# program created by mohit
# offical website L4wisdom.com
# email-id  mohitraj.cs@gmail.com
import os
from threading import Thread
import cPickle
import argparse
from collections import OrderedDict
from datetime import datetime, timedelta
import time
import shutil
from colorama import init,Fore, Back, Style
import urllib
import re
import subprocess
import webbrowser
import dateutil.parser
import time

init(autoreset=True)
class file_backup():
    dict1 = {}
    def __init__(self):
        pass

    def version_get(self,version1):
        url2 = 'http://l4wisdom.com/fdate.php'
        try:
            http_r = urllib.urlopen(url2)
            for each in http_r:
                if 'Current Version' in each:
                    cur_version = float(each.split('=')[1].strip("\n"))
            if cur_version>version1:
                print( Back.RED +'Please download latest code')

        except :
            pass

    def get_drives(self):
        response = os.popen("wmic logicaldisk get caption")
        list1 = []
        for line in response.readlines():
            line = line.strip("\n")
            line = line.strip("\r")
            line = line.strip(" ")
            if (line == "Caption" or line == ""):
                continue
            list1.append(line)
        return list1

    def file_open(self):
        pickle_file = open("fdate.raj", "r")
        file_dict = cPickle.load(pickle_file)
        pickle_file.close()
        return file_dict

    def strore_files(self):
        pickle_file = open("fdate.raj", "w")
        cPickle.dump(file_backup.dict1, pickle_file)
        pickle_file.close()
    def search1(self, drive):
        file_t= open("Error_fdate.txt",'w')
        for root, dir, files in os.walk(drive, topdown=True):
            for file in files:
                file = file.lower()
                file_path = root+'\\'+file
                #print file_path
                try:
                    creation_time = os.path.getctime(file_path)
                    modification_time = os.path.getmtime(file_path)
                    tuple1  = (creation_time,modification_time)
                    file_backup.dict1[file_path]  = tuple1

                except Exception as e :
                    str1 = str(e)+'\n'
                    file_t.write(str1)
        file_t.close()

    def copy_files(self, path_to_copy, files,m_or_c=0 ):
        try:
            for file in files:
                if m_or_c==0:
                    shutil.copy(file,path_to_copy)
                    print file," Copied"
                else :
                    shutil.move(file, path_to_copy)
                    print file, " Moved"
        except Exception as e :
            print e

    @staticmethod
    def matching_string(match1, all_file):
        maching_files = {}
        for k,v in all_file.iteritems():
            if re.search(match1,k):
                maching_files[k]=v

        return maching_files

    @staticmethod
    def filter_list(e_list,all_files):
        for each in all_files.keys():
            each1= each.lower()
            for e in e_list:
                e = e.lower()
                if each1.startswith(e):
                    del all_files[each]
        return all_files

    @staticmethod
    def file_run(path1):
        path = path1[2:]
        file_list = path.split("\\")
        os.chdir(path1[0:2] + '//')
        file_to_open = file_list[-1]
        file_list= file_list[:-1]
        if file_list[0]:
            for each in file_list:
                os.chdir(each)
        file_name = '"' + file_to_open + '"'
        os.startfile(file_name)

    @staticmethod
    def folder_open(path):
        print "path*****", path
        path = path.rsplit("\\", 1)[0]
        path_list = path.split("\\")
        # print path_list
        os.chdir(path_list[0][0:2])
        if path_list[0][2:]:
            os.chdir(path_list[0][2:])
        if len(path_list) > 1:
            for i in xrange(1, len(path_list) - 1):
                os.chdir(path_list[i])
            os.chdir(path_list[-1].split(":")[0])
        subprocess.Popen(r'explorer /select,"." ')

    def file_get(self,time_stamp,latest=None,m=0, order= False, number_of_files=0,e_list=None,match=None):
        a = (Fore.RED + '-----------------------------------------------------------------')
        b = (Fore.BLUE + '|')
        t1 = datetime.now()
        i = 0
        d1 = {}
        all_file = self.file_open()
        if not latest:
            latest = time.time()

        if e_list:   #Exception list
            all_file=self.filter_list(e_list,all_file)
        if match:
            all_file= self.matching_string(match,all_file)
        for key,values in all_file.iteritems():
            c_date = values[m]
            if c_date>= time_stamp and c_date<= latest:
                d1[key]= c_date
        d2 = OrderedDict(sorted(d1.items(), key=lambda (k, v): v, reverse=order))

        for k,v in d2.iteritems():
            i = i + 1
            print i, ": ", k, b ,time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime(v))
            print a
            if i== number_of_files:
                break

        print "Total files are ", i
        t2 = datetime.now()
        total_time = t2 - t1
        print "Time taken ", total_time
        try:
            if i:
                ch = raw_input("Press D to open folder or F to open file or M to move files or C to copy files\t")
                ch = ch.lower()
                if ch == 'c' or ch=='m':
                    n = raw_input('Enter the number of the files for multiple files give number with space or type "ALL" for all files \t')
                    d = raw_input('Enter the path \t ')
                    if n =='ALL':
                        files = d2.keys()

                    else :
                        numbers = n.split()
                        print numbers
                        files = [d2.keys()[int(num)-1] for num in numbers]
                    if ch == 'c':
                        self.copy_files(d,files)
                    elif ch== 'm':
                        self.copy_files(d,files,m_or_c=1)

                elif ch=='d' or ch=='f':
                    num = int(raw_input("Enter the number \t"))
                    path=d2.keys()[num-1]
                    if ch=='d':
                        self.folder_open(path)
                    elif ch=='f':
                        self.file_run(path)
        except Exception as e :
            print e

def create():
    t1 = datetime.now()
    list2 = []  # empty list is created
    obj1 = file_backup()
    list1 = obj1.get_drives()
    print "Creating Index..."
    for each in list1:
        process1 = Thread(target=obj1.search1, args=(each,))
        process1.start()
        list2.append(process1)

    for t in list2:
        t.join()  # Terminate the threads
    obj1.strore_files()
    t2 = datetime.now()
    Total_time = t2-t1
    print "Time taken ", Total_time
    print "Open Error_fdate.txt to check the exceptions "

def time1(t,num):
    num = eval(num)
    if t=='s':
        delta = timedelta(seconds=num)
    elif t=='m':
        delta = timedelta(minutes=num)
    elif t=='h':
        delta = timedelta(hours=num)
    elif t=='d':
        delta = timedelta(days=num)

    times= datetime.now() - delta
    t1 = times.strftime('%Y-%m-%d %H:%M:%S')
    time_stamp = int(time.mktime(time.strptime(t1, '%Y-%m-%d %H:%M:%S')))
    return time_stamp

def time2(t):
    date1 = dateutil.parser.parse(t)
    t1 = date1.strftime('%Y-%m-%d %H:%M:%S')
    time_stamp = int(time.mktime(time.strptime(t1, '%Y-%m-%d %H:%M:%S')))
    return time_stamp

def all_flags(R,n,e,m,M):
    reverse_flag = False

    files = 0
    list1 = []
    mod_flag = 0
    str_match = None
    if R:
        reverse_flag = True
    if n:
        files = n
    if e:
        list1 = e
    if m:
        str_match = m
    if M:
        mod_flag = 1
    return (reverse_flag,files,list1,str_match,mod_flag)

def main():
    version1=2.1
    parser = argparse.ArgumentParser(version=str(version1))
    parser.add_argument('-a', action='store_true', help='Know more about Author Mohit')
    parser.add_argument('-cs', nargs='?', help='for seconds according to creation date, Main option ')
    parser.add_argument('-cm', nargs='?', help='for minute according to creation date, Main option ' )
    parser.add_argument('-ch', nargs='?', help='for hours according to creation date, Main option' )
    parser.add_argument('-cd', nargs='?', help='for days according to creation date, Main option', )
    parser.add_argument('-et', nargs='?', help='Exact date like 2015-10-28 16:09:59 , Main option', )
    parser.add_argument('-M', action='store_true', help='Search according to modification date, use with main option')
    parser.add_argument('-R', action='store_true',help='To display the file in reverse oorder, use this option with Main options')
    parser.add_argument('-l', nargs='?',help='To set the range, use this option with Main options to provide lower timestamp ' )
    parser.add_argument('-n', nargs='?',help='To display limited files, use this option with Main options',type=int,default=0)
    parser.add_argument('-e', nargs='+', help='To display the files except for mentioned files with the option, use this option with Main options',default=None)
    parser.add_argument('-m', nargs='?', help='Get the files with matching string, use this option with Main options')

    args = parser.parse_args()
    obj2 = file_backup()
    try:

        time_stamp = False
        time_2 = False

        if args.cs:
            time_stamp = time1('s', args.cs)
            if args.l:
                if eval(args.l) < eval(args.cs):
                    time_2 = time1('s', args.l)
                else:
                    print "Second range must be small"

            reverse_flag, files, list1, str_match, mod_flag = all_flags(args.R,args.n,args.e,args.m,args.M)


        elif args.cm:
            time_stamp = time1('m', args.cm)
            if args.l:
                if eval(args.l) < eval(args.cm):
                    time_2 = time1('m', args.l)
                else:
                    print "Second range must be small"

            reverse_flag, files, list1, str_match, mod_flag = all_flags(args.R, args.n, args.e, args.m, args.M)

        elif args.ch:
            time_stamp = time1('h', args.ch)
            if args.l:
                if eval(args.l) < eval(args.ch):
                    time_2 = time1('h', args.l)
                else:
                    print "Second range must be small"

            reverse_flag, files, list1, str_match, mod_flag = all_flags(args.R, args.n, args.e, args.m, args.M)

        elif args.cd:
            time_stamp = time1('d', args.cd)
            if args.l:
                if eval(args.l) < eval(args.cd):
                    time_2 = time1('d', args.l)
                else:
                    print "Second range must be small"

            reverse_flag, files, list1, str_match, mod_flag = all_flags(args.R, args.n, args.e, args.m, args.M)

        elif args.et:
            time_stamp = time2( args.et)
            time_2 = time2(args.l)

            reverse_flag, files, list1, str_match, mod_flag = all_flags(args.R, args.n, args.e, args.m, args.M)


        elif args.a:
            url = 'https://www.packtpub.com/books/info/authors/mohit'
            webbrowser.open(url)

        if time_stamp:
            obj2.file_get(time_stamp, latest=time_2, m=mod_flag, order=reverse_flag, number_of_files=files, e_list=list1,match=str_match)

        elif args.a:
            pass
        else :
            create()
            obj2.version_get(version1)
        str1 = (Back.MAGENTA + 'L4wisdom.com')
        print "\nThanks for using "+str1
        print(Back.CYAN + 'Email id mohitraj.cs@gmail.com')
        print "For updated version or help, browse our page  http://l4wisdom.com/fdate.php"

    except Exception as e:
        print e
        print "Please use proper format to search a file use following instructions"
        print "see file-name"
        print "Use <see -h >  For help"

if __name__== '__main__':
    main()
