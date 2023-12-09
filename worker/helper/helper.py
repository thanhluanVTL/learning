import json, pytz, uuid
from datetime import datetime
from handler.s3 import MinioHandler
from io import BytesIO
from utils.utils import getenv

date_format = "%Y-%m-%d"
datetime_format = "%Y-%m-%d %H:%M:%S"

def get_current_date(type:str):
    if type=="date":
        return datetime.now(pytz.timezone(getenv("TIMEZONE"))).strftime(date_format)
    elif type=="datetime":
        return datetime.now(pytz.timezone(getenv("TIMEZONE"))).strftime(datetime_format)
    else:
        print("type must be date or datetime")

def object_name_generator(str_date:str, task_id:str, extension:str) -> str:
    return f"{str_date}/{task_id}.{extension}"

def dict_to_json_s3(task_id:str, data:dict):
    json_bytes = json.dumps(data, indent=2, ensure_ascii=False).encode("utf-8")
    json_buffer = BytesIO(json_bytes)

    s3 = MinioHandler()

    object_link = s3.upload_file(object_name=object_name_generator(str_date=get_current_date(type="date"), task_id=task_id, extension="json"),
                                 data=json_buffer,
                                 length=len(json_bytes)
                                 )
    return object_link

import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))