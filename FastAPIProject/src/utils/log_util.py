import logging
from logging import StreamHandler
from logging.handlers import RotatingFileHandler
import os
import sys


class LogFactory:
    """
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0
    """
    logging_levels = {
        "CRITICAL": logging.CRITICAL,
        "FATAL": logging.FATAL,
        "ERROR": logging.ERROR,
        "WARNING": logging.WARNING,
        "WARN": logging.WARN,
        "INFO": logging.INFO,
        "DEBUG": logging.DEBUG,
        "NOTSET": logging.NOTSET
    }

    filepath = "logs/fastapi.log"
    format = "%(asctime)s | %(levelname)s | %(pathname)s | %(process)s | %(processName)s | " +\
        "%(filename)s | %(funcName)s | %(lineno)d | %(message)s | %(name)s"

    date_format = "%b-%d-%Y %H:%M:%S"
    log_file_name = "logs/fastapi.log"

    @classmethod
    def configure_logger(cls, logger_name=None, logging_level=None):
        # Initializing logger
        service_logger = (
            logging.getLogger(name=logger_name) if logger_name else logging.getLogger()
        )

        if logging_level not in cls.logging_levels:
            logging_level = "WARN"
        service_logger.setLevel(logging_level)
        # Creating logs directory
        os.makedirs(os.path.dirname(cls.log_file_name), exist_ok=True)
        # Defining handlers
        file_handler = RotatingFileHandler(
            "C:/Users/mukesh/Downloads/Python-FastAPI/FastAPIProject/src/utils/logs/fastapi.log",
            maxBytes=1048576,
            backupCount=5,
            encoding="utf-8"
        )
        std_out_handler = StreamHandler(stream=sys.stdout)

        # Defining the formatter
        formatter = logging.Formatter(fmt=cls.format, datefmt=cls.date_format)
        # Adding formatter to handlers
        file_handler.setFormatter(formatter)
        std_out_handler.setFormatter(formatter)

        # Adding handlers to logger
        service_logger.addHandler(file_handler)
        service_logger.addHandler(std_out_handler)
        service_logger.debug("The logger configured")


service_logger_name = "fastapi_service"
LogFactory.configure_logger(logger_name=service_logger_name,
                            logging_level=os.environ.get("LOGGING_LEVEL", "DEBUG"))

logger = logging.getLogger(service_logger_name)


