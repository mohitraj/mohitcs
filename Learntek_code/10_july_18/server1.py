import ConfigParser

config = ConfigParser.ConfigParser()

config.read("Server_conf.ini")

web_ip = config.get("WebServer","IP")
web_port = int(config.get("WebServer","port"))

print web_ip, web_port, type(web_ip), type(web_port)

sql_ip = config.get("SQL","IP")
sql_port = int(config.get("SQL","port"))

print sql_ip, sql_port