from utils.utils import getenv
from minio import Minio

s3 = {
    "endpoint":getenv("S3_ENDPOINT"),
    "access_key":getenv("S3_KEY"),
    "secret_key":getenv("S3_SECRET")
}

s3_client = Minio(
    endpoint=getenv("S3_ENDPOINT")[7:],
    access_key=getenv("S3_KEY"),
    secret_key=getenv("S3_SECRET"),
    secure=False
)

storage_options = {
        "key": getenv("S3_KEY"), 
        "secret": getenv("S3_SECRET"), 
        "client_kwargs": {
            "endpoint_url": getenv("S3_ENDPOINT")
        }
    }
