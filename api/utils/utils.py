import os
from dotenv import load_dotenv

def getenv(str_key):
    load_dotenv()
    key = os.environ.get(str_key)
    return key