import json
import logging
import sys
import time

from app.utils.settings import settings


class JsonFormatter(logging.Formatter):
    datetime_format = '%Y-%m-%d %H:%M:%S'

    def __init__(
        self,
        in_docker,
        fmt=None,
        datefmt=None,
        style='%',
    ):
        logging.Formatter.__init__(self, fmt, datefmt, style)
        self.in_docker = in_docker

    def format(self, record):
        data = {
            'datetime': self.formatTime(record),
            'levelname': record.levelname,
            'module': record.name,
            'function': record.funcName,
            'lineno': record.lineno,
            'message': record.msg,
        }
        if self.in_docker:
            return json.dumps(data, ensure_ascii=False)
        return json.dumps(data, indent=2, ensure_ascii=False)

    def formatTime(self, record):
        converter = time.localtime
        ct = converter(record.created)
        s = time.strftime(self.datetime_format, ct)
        return s


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(JsonFormatter(settings.IN_DOCKER))
    return console_handler


def get_logger(logger_name: str):
    logger = logging.getLogger(logger_name)
    if settings.DEBUG:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    logger.addHandler(get_console_handler())
    logger.propagate = False
    return logger
