import threading
import logging
logging.basicConfig(filename="live1.log",filemode="w", level=logging.CRITICAL)
logging.debug("This is a debug message")
logging.info("Informational message")
logging.warning("A warning!")
logging.error("An error has happened!")
logging.critical("Critical !!!!")

print (threading.activeCount())