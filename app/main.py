from datetime import datetime
from pytz import timezone
import uvicorn
from fastapi import FastAPI
import logging
import logging.config

import time, random, string
from requests import Request

from function.function import sum_2

from loggers.loggers import stream_log, debug_log, info_log, warning_log, error_log

logger = logging.getLogger(__name__)

# logger.addHandler(stream_log)
logger.addHandler(debug_log)
logger.addHandler(info_log)
logger.addHandler(warning_log)
logger.addHandler(error_log)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")
    # logger.error(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")
    
    return response

@app.get("/")
async def root():
    logger.debug("Debug == Luan")
    logger.info("logging from the root logger")
    logger.warning("Warning == Luan")
    logger.error("Error == Luan")
    return {"message": "Hello World"}
    

@app.get("/users")
async def users():
    logger.info(f"request / endpoint!")
    users = [
        {
            "name": "Mars Kule",
            "age": 25,
            "city": "Lagos, Nigeria"
        },

        {
            "name": "Mercury Lume",
            "age": 23,
            "city": "Abuja, Nigeria"
        },

         {
            "name": "Jupiter Dume",
            "age": 30,
            "city": "Kaduna, Nigeria"
        }
    ]

    return users

@app.get("/test")
async def test():
    logger.info(f"request /test endpoint!")
    result = [
        {
            "sum": sum_2(5, 55)
        }
    ]

    return result

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)