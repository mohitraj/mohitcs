import logging

logging.basicConfig(filename= "live.log",filemode='w',level=logging.CRITICAL)

# debug, info, warning , error, critical

logging.debug("This is the debug message")
logging.info("This is the INFO message")
logging.warning("This is the WARNING message")
logging.error("This is the eRROR message")
logging.critical("This is the cRITICAL message")