import logging
from loggers.loggers import error_log, debug_log
logger = logging.getLogger("function")
logger.addHandler(error_log)
logger.addHandler(debug_log)

def sum_2(a, b):
    logger.info("START FUNCTION")
    c = a+b
    logger.debug(f"RESULT IS: {c}")
    logger.error("FINISHED FUNCTION")
    return c
