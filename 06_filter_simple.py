import logging 


def filter_start_x(record: logging.LogRecord):
    # print(record.__dict__)
    if record.msg.startswith("x"):
        return False
    return True


logger = logging.getLogger()

logger.warning("this is a message 1")

logger.addFilter(filter_start_x)

logger.warning("this is a message 2")
logger.warning("x this is a message 3")