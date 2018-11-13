import logging
logger = logging.getLogger("Learntek")
logger.setLevel(logging.ERROR)
fh = logging.FileHandler("live1.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)