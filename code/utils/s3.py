from minio import Minio

def file_path_generator(s3_bucket, file_path):
    print("File Path Generator")
    if file_path[0] == "/":
        file_path = f"s3://{s3_bucket}{file_path}"
        print(file_path)
        return file_path
    else:
        file_path = f"s3://{s3_bucket}/{file_path}"
        print(file_path)
        return file_path

def storage_options_generator(s3:dict):
    try:
        if all(key in s3 for key in ("endpoint", "access_key", "secret_key")):
            endpoint = s3.get("endpoint")
            access_key = s3.get("access_key")
            secret_key = s3.get("secret_key")
            storage_options= {
                "key": access_key,
                "secret": secret_key,
                "client_kwargs": {
                    "endpoint_url": endpoint
                }
            }
            return storage_options
    except KeyError as e:
        print(e)

def client_generator(s3:dict):
    try:
        if all(key in s3 for key in ("endpoint", "access_key", "secret_key")):
            endpoint = s3.get("endpoint")
            access_key = s3.get("access_key")
            secret_key = s3.get("secret_key")

            client = Minio(
                endpoint=endpoint[7:],
                access_key=access_key,
                secret_key=secret_key,
                secure=False
                )
            return client
    except KeyError as e:
        print(e)

def objectExists(client, bucket_name, path:str, recursive:bool = False):
    objects = client.list_objects(bucket_name=bucket_name, prefix=path, recursive=recursive)
    # for obj in objects:
    #     print(obj.object_name)
    obj_list = list(objects)
    print(obj_list)
    # for obj in obj_list:
    #     print(obj.object_name)

    print(list(obj.object_name for obj in obj_list))
    
    if len(obj_list) > 0:
        return True
    elif len(obj_list) == 0:
        return False


def bucketExists(client, bucket_name):
    if client.bucket_exists(bucket_name):
        # print("my-bucket exists")
        return True
    else:
        # print("my-bucket does not exist")
        return False