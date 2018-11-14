import os
import sys


list1 = ['192.168.0.1','192.168.56.1','192.168.23.1', '127.0.0.1' ]

if sys.platform =='linux':
	cmd = "ping -c 1 "
elif sys.platform=="win32":
	cmd = "ping -n 1 "
else :
	cmd = "ping -c 1 "

for ip in list1:
	cmd1 = cmd+ip
	resp=os.popen(cmd1)
	text = resp.read()
	print (cmd1)
	
	if "ttl" in text.lower():
		print (ip, " is live")
	else :
		print (ip, " is NOT live")
