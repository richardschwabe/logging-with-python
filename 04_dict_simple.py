import logging 
from logging.config import dictConfig

config = {
    'version':1, 
    "disable_existing_loggers": False, 
    'formatters':{
        'standard': {
            "format": '%(levelname)-10s:%(message)s'
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
        }
    }
}

dictConfig(config)

logging.critical("Its critical")
logging.error("Its error")
logging.warning("Its warning")
logging.info("Its info")
logging.debug("Its debug")