import ConfigParser

config = ConfigParser.ConfigParser()

config.read("Server_conf.ini")

for each in  config.sections():  # ['WebServer', 'SQL']

	#print config.items(each)  #[('ip', '127.0.0.1'), ('port', '80')]
	print "\n",each, "\n"
	for k,v in config.items(each):
		print k, " : ",v