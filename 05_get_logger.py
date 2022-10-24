import logging 
from logging.config import dictConfig

config = {
    'version':1, 
    "disable_existing_loggers": False, 
    'formatters':{
        'standard': {
            "format": '%(levelname)-10s:%(name)s:%(message)s'
        }
    }, 
    'handlers': {
        'default': {
            'level': "DEBUG",
            "formatter": "standard", 
            "class": "logging.StreamHandler", 
            "stream": "ext://sys.stdout"
        },
        "file": {
            "level": "WARNING", 
            'formatter': "standard",
            'class': "logging.FileHandler", 
            'filename': "logs/dict_simple.log",
            'mode': "w"
        }
    },
    'loggers': {
        "": {
            'level': "DEBUG",
            'handlers': ['default', 'file'], 
            'propagate': True
        },
        "richard": {
            'level': "INFO",
            'handlers': ['default'], 
            'propagate': False
        }
    }
}

dictConfig(config)

my_logger = logging.getLogger("richard")


my_logger.critical("Its critical")
my_logger.error("Its error")
my_logger.warning("Its warning")
my_logger.info("Its info")
my_logger.debug("Its debug")