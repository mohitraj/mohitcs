import logging

logging.basicConfig(filename= "live1.log", filemode='w', level= logging.CRITICAL)

logging.debug("This is debug message")
logging.info("This is information message")
logging.warning("A warning")
logging.error("error occurred")
logging.critical("Critical")
