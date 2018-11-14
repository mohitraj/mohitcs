import configparser

config = configparser.ConfigParser()

config.read("server_config.ini")

for section in config.sections():  #['SQL', 'DNS', 'WebServer']
	print (section)
	for fix, value in config.items(section): #[('server_ip', '127.0.0.1'), ('port', '3306')]
		print (fix, " : ", value)
		
#print (config.options('DNS'))  #['server_ip', 'port']

