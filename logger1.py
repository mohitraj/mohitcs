import logging
logger = logging.getLogger("Mohit")
logger.setLevel(logging.INFO)
fh = logging.FileHandler("Sync.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)