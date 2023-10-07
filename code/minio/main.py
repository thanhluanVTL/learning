from minio_handler import MinioHandler

minio_client = MinioHandler()

bucket_name = "test"

# minio_client.check_connection()
# minio_client.make_bucket(bucket_name)
# minio_client.check_file_name_exists(bucket_name, "get_all_cust_1.parquet")

list_objects = minio_client.list_objects(bucket_name)
# list_objects = minio_client.list_objects(bucket_name, prefix="aaaa", recursive=True)
# list_objects = minio_client.check_object_exist(bucket_name, prefix="a", recursive=True)
# list_objects = minio_client.check_object_exists_by_name(bucket_name, file_name="a/get_all_custaa.parquet")

print(list_objects)

# # df = minio_client.read_parquet_to_df(bucket_name, object_name="a/get_all_cust.parquet")
# df = minio_client.read_parquet_to_df(bucket_name, object_name_prefix="get_all_cust.parquet")
# print(df)

df = minio_client.read_list_parquet_to_df(bucket_name, object_name_prefix="get_all_cust")
print(df)
