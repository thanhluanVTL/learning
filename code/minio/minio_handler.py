import random
from datetime import datetime, timedelta

from utils import getenv

from minio import Minio
# from urllib3.exceptions import MaxRetryError
# import urllib3

import io
import pandas as pd

import pyarrow as pa
import pyarrow.parquet as pq
from pyarrow import Table

import logging


logger = logging.getLogger(__name__)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.basicConfig(level=logging.INFO)




class MinioHandler():
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if not MinioHandler.__instance:
            MinioHandler.__instance = MinioHandler()
        return MinioHandler.__instance

    def __init__(self):
        self.minio_url = getenv("MINIO_URL")
        self.access_key = getenv("MINIO_ACCESS_KEY")
        self.secret_key = getenv("MINIO_SECRET_KEY")
        self.client = Minio(
            self.minio_url,
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=False
        )

    def check_connection(self):
        try:
            self.client.list_buckets()
            return True
        except Exception:
            logging.critical("Object storage not reachable")


    def make_bucket(self, bucket_name) -> str:
        try:
            if not self.client.bucket_exists(bucket_name):
                self.client.make_bucket(bucket_name)
                logging.info("Bucket created")
                return bucket_name
            else:
                logging.info("Bucket already existed")
                return bucket_name
        except Exception:
            logging.critical("Object storage not reachable")

    def list_objects(self, bucket_name, prefix=None, recursive=False):
        try:
            objects = self.client.list_objects(bucket_name, prefix, recursive)
            return list(object.object_name for object in objects)
        except Exception as e:
            logging.ERROR(e)
    
    def check_object_exist(self, bucket_name, prefix=None, recursive=False):
        try:
            objects = self.client.list_objects(bucket_name, prefix, recursive)
            if len(list(object.object_name for object in objects)) > 0:
                return True
            else:
                logging.info("Object does not exist")
                return False
        except Exception as e:
            logging.ERROR(e)
            
    def check_object_exists_by_name(self, bucket_name, file_name):
        try:
            self.client.stat_object(bucket_name=bucket_name, object_name=file_name)
            return True
        except Exception as e:
            print(e.message)
            return False

    def read_parquet_to_df(self, bucket_name, object_name_prefix):
        try:
            if self.check_object_exist(bucket_name=bucket_name, prefix=object_name_prefix):
                file = self.client.get_object(bucket_name, object_name_prefix).read()
                reader = pa.BufferReader(file)
                table = pq.read_table(reader)
                data_df = table.to_pandas()
                return data_df
            else:
                logging.info("Parquet file not exist")
                return pd.DataFrame()
        except Exception as e:
            # print(e.message)
            logging.ERROR(e)
    
    def read_list_parquet_to_df(self, bucket_name, object_name_prefix, recursive=False):
        try:
            list_objects = self.list_objects(bucket_name=bucket_name, prefix=object_name_prefix, recursive=recursive)
            data_df = pd.DataFrame()
            if len(list_objects) > 0:
                for object in list_objects:
                    df = self.read_parquet_to_df(bucket_name=bucket_name, object_name_prefix=object)
                    if len(data_df)==0:
                        data_df = df
                    else:
                        data_df = pd.concat([data_df, df])
                return data_df
            else:
                logging.info("Parquet files not exist")
                return data_df
        except Exception as e:
            logging.ERROR(e)

            

        


    