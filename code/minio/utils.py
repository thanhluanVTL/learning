import os
import datetime
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime, timedelta, date

def getenv(str_key):
    load_dotenv()
    key = os.environ.get(str_key)
    return key