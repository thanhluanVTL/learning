from datetime import datetime
from pytz import timezone
import logging

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

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# logging.basicConfig(filename="logs/app_logs.log", filemode='a', format="%(asctime)s %(name)s %(levelname)s %(message)s", level=logging.DEBUG)
# logging.basicConfig(filename="/simple_app/logs/app_logs.log", filemode='a', format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s", level=logging.INFO)

stream_log = logging.StreamHandler()
stream_log.setFormatter(logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s"))
stream_log.setLevel(logging.INFO)

#to log debug messages                               
debug_log = logging.FileHandler("logs/debug.log")
debug_log.setFormatter(logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s"))
debug_log.setLevel(logging.DEBUG)
debug_log.addFilter(LoggingLevelFilter(logging.DEBUG))

info_log = logging.FileHandler("logs/info.log")
info_log.setFormatter(logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s"))
info_log.setLevel(logging.INFO)
info_log.addFilter(LoggingLevelFilter(logging.INFO))

warning_log = logging.FileHandler("logs/warning.log")
warning_log.setFormatter(logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s"))
warning_log.setLevel(logging.WARNING)
warning_log.addFilter(LoggingLevelFilter(logging.WARNING))

#to log errors messages
error_log = logging.FileHandler("logs/error.log")
error_log.setFormatter(logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s"))
error_log.setLevel(logging.ERROR)

# logger.addHandler(debug_log)
# logger.addHandler(error_log)
# logger.addHandler(stream_log)