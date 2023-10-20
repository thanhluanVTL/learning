from datetime import datetime
from pytz import timezone
import logging
from logging import config

class LoggingLevelFilter(logging.Filter):
    def __init__(self, logging_level: int):
        super().__init__()
        self.logging_level = logging_level

    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelno == self.logging_level

def timetz(*args):
    return datetime.now(tz).timetuple()

tz = timezone('Asia/Ho_Chi_Minh')

logging.Formatter.converter = timetz

logging_config = {
    'version': 1,
    'formatters': {
        'debug_formatter': {
            'format': '{asctime} - {name} - {levelname} - {message}',
            'style': '{',
            'datefmt': '%Y-%m-%d %H:%M:%S.%f',
        },
        'infor_formatter': {
            'format': '{asctime} - {name} - {levelname} - {message}',
            'style': '{',
            'datefmt': '%Y-%m-%d %H:%M:%S.%f',
        },
        'warning_formatter': {
            'format': '{asctime} - {name} - {levelname} - line {lineno} - {message}',
            'style': '{',
            'datefmt': '%Y-%m-%d %H:%M:%S.%f',
        },
        'error_formatter': {
            'format': '{asctime} - {name} - {levelname} - line {lineno} - {message}',
            'style': '{',
            'datefmt': '%Y-%m-%d %H:%M:%S.%f',
        },
    },
    # 'filters': {
    #     'file_filter': {
    #         '()': FileFilter,
    #     },
    # },
    'handlers': {
        'console_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'debug_formatter',
        },
        'debug_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'debug_formatter',
            'level': 'DEBUG',
            # 'filters': ['file_filter'],
            'filename': 'logs/debug.log',
        },
        'info_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'debug_formatter',
            'level': 'INFO',
            'filename': 'logs/info.log',
        },
        'warning_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'debug_formatter',
            'level': 'WARNING',
            'filename': 'logs/warning.log',
        },
        'error_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'error_formatter',
            'level': 'ERROR',
            'filename': 'error.log',
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console_handler', 'debug_handler', 'info_handler', 'warning_handler', 'error_handler'],
    },
}

config.dictConfig(logging_config)

logger = logging.getLogger(__name__)

# these get logged to the console and only to the debugs.log file
# if you want just the debug messages logged to the file, adjust the filter
logger.debug('this is a debug message')
logger.info('this is an info message')
logger.warning('this is a warning message')

# this get logged to the console and only to the errors.log file
logger.error('this is an error message')
logger.critical('this is a critical message')