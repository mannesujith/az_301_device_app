
import logging
from logging.config import dictConfig

LOGGING_CONFIG = {
  "handlers": {
    "h": {
      "backupCount": 5,
      "level": "DEBUG",
      "encoding": "utf8",
      "filename": "logs.log",
      "maxBytes": 5242880,
      "formatter": "simple",
      "class": "logging.handlers.RotatingFileHandler"
    },
    
  },
  "version": 1,
  "root": {
    "level": 10
  },
  "loggers": {
    "rest_log": {
      "handlers": [
        "h"
      ],
      "propagate": True
    },
    
  },
  "formatters": {
    "simple": {
      "format": "%(levelname)s %(asctime)s {function name : %(funcName)s Line no : %(lineno)d} %(message)s"
    }
  }
}
dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(name='rest_log')