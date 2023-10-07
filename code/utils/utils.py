import os
import datetime
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime, timedelta, date

def getenv(str_key):
    load_dotenv()
    key = os.environ.get(str_key)
    return key

def ListToString(strlist:list, split:str):
    # outstring = ", ".join([str(item) for item in strlist])
    outstring = split.join([str(item) for item in strlist])
    # print(outstring)
    return outstring

def date_key_generator(str_date):
    txt_list = str_date.split("-")
    # date_s = ''.join(txt_list)
    date_s = ListToString(strlist=txt_list, split="")
    return int(date_s)

def crete_directory(str_path):
    Path(str_path).mkdir(parents=True, exist_ok=True)

def date_validate(str_date:str):
    try:
        date.fromisoformat(str_date)
        # datetime.date.fromisoformat(str_date)
        return str_date
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def get_default_date(str_date:str=None):
    if str_date == None:
        str_date_default = (datetime.now()-timedelta(days = 1)).strftime("%Y-%m-%d")
    else:
        str_date_default = date_validate(str_date)
    return str_date_default