from datetime import datetime
from pytz import timezone
import uvicorn
from fastapi import FastAPI
import logging
import logging.config

import time, random, string
from requests import Request

from function.function import sum_2

def timetz(*args):
    return datetime.now(tz).timetuple()

tz = timezone('Asia/Ho_Chi_Minh')

logging.Formatter.converter = timetz

logging.basicConfig(filename="logs/app_logs.log", filemode='a', format="%(asctime)s %(name)s %(levelname)s %(message)s", level=logging.DEBUG)
# logging.basicConfig(filename="/simple_app/logs/app_logs.log", filemode='a', format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s", level=logging.INFO)


# logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# logger = logging.getLogger("luan")
logger = logging.getLogger(__name__)

stream_log = logging.StreamHandler()
stream_log.setFormatter(logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s"))
stream_log.setLevel(logging.INFO)

#to log debug messages                               
debug_log = logging.FileHandler("logs/debug.log")
debug_log.setFormatter(logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s"))
debug_log.setLevel(logging.DEBUG)

#to log errors messages
error_log = logging.FileHandler("logs/error.log")
error_log.setFormatter(logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s"))
error_log.setLevel(logging.ERROR)

logger.addHandler(debug_log)
logger.addHandler(error_log)
logger.addHandler(stream_log)

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
    logger.info("logging from the root logger")
    logger.debug("Debug == Luan")
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
            "city": "Kaduna, Nigeria",
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