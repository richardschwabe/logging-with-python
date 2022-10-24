import logging 

logging.basicConfig(level=logging.DEBUG, filename="logs/basic.log", filemode="w", encoding="utf-8")

logging.critical("Its critical")
logging.error("Its error")
logging.warning("Its warning")
logging.info("Its info")
logging.debug("Its debug")