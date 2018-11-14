import configparser

config = configparser.ConfigParser()

config.read("server_config.ini")

print (config.get('SQL','Server_ip'))
DNS_Port=  int((config.get('SQL','Port')))

print((DNS_Port))