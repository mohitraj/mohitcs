import ConfigParser

config = ConfigParser.ConfigParser()



file_w = open("Server_conf.ini","a+")

config.add_section("FTP")
config.set("FTP","IP","127.0.0.1")
config.set("FTP","port", 21)

config.write(file_w)

file_w.close()