from utils.extract import data_extraction_from_s3
from s3.configs import s3, s3_client
from utils.utils import getenv
from utils.s3 import objectExists

s3_bucket_src = getenv("S3_BUCKET")

cust_file_path = f"/get_all_cust.parquet"
cust_columns = ['c_customer_code', 'c_customer_type', 'c_cust_birth_day', 'c_cust_gender', 'c_create_time', 'c_authen_acc_status', 'c_authen_bo_status', 'c_authen_sign']

# customers = data_extraction_from_s3(s3=s3, bucket_name=s3_bucket_src, file_path=cust_file_path, columns=cust_columns)
# print(customers)

prefix = f"get_all_cust"
print(objectExists(client=s3_client, bucket_name=s3_bucket_src, path=prefix, recursive=True))