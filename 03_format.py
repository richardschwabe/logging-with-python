import logging 

logging.basicConfig(level=logging.DEBUG, format='%(levelname)-10s:%(name)s:%(message)s')

logging.critical("Its critical")
logging.error("Its error")
logging.warning("Its warning")
logging.info("Its info")
logging.debug("Its debug")