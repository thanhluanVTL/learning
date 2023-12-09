from utils.utils import getenv
from minio import Minio
import logging

class MinioHandler():
    def __init__(self):
        self.minio_url_scheme = getenv("MINIO_URL_SCHEME")
        self.minio_url = getenv("MINIO_URL")
        self.minio_access_key = getenv("MINIO_ACCESS_KEY")
        self.minio_secret_key = getenv("MINIO_SECRET_KEY")
        self.client = Minio(
            self.minio_url,
            access_key=self.minio_access_key,
            secret_key=self.minio_secret_key, 
            secure=False
            )
        
        self.bucket = getenv("MINIO_BUCKET_NAME")
    
    def check_connection(self):
        try:
            self.client.list_buckets()
            return True
        except Exception:
            logging.info("Object storage not reachable")
            return False
    
    def upload_file(self, object_name, data, length):
        self.client.put_object(
            bucket_name=self.bucket,
            object_name=object_name,
            data=data,
            length=length
        )
        return f"http://127.0.0.1:9000/{self.bucket}/{object_name}"