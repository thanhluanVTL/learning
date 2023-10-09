import random
from datetime import datetime, timedelta
from utils import getenv
import pandas as pd


import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class PandasHandler():
    
    def __init__(self):
        self.endpoint_url = getenv("MINIO_URL_SCHEME")
        self.key = getenv("MINIO_ACCESS_KEY")
        self.secret = getenv("MINIO_SECRET_KEY")
        self.storage_options = {
            "key" : self.key,
            "secret" : self.secret,
            "client_kwargs" : 
            {
                "endpoint_url" : self.endpoint_url
            }
        }
    
    def read_parquet_s3(self, path, engine:str="fastparquet", columns:list=None):
        try:
            df =pd.read_parquet(
                path=path,
                engine=engine,
                storage_options=self.storage_options,
                columns=columns
            )
            return df
        except Exception as e:
            print(f"Exception: {e}")


    