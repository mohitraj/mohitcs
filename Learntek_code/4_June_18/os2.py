import os

resp= os.popen("ping 127.0.0.1")

results = resp.read()
#print results
if 'ttl' in results.lower():
	print "IP is live"