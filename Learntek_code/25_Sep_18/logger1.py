import logging
logger = logging.getLogger("LearnTek")
logger.setLevel(logging.INFO)
fh = logging.FileHandler("live2.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)