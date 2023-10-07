import tempfile
import pandas as pd
# import dask.dataframe as dd
from utils.utils import getenv
from s3.configs import storage_options
from utils.s3 import storage_options_generator, client_generator, objectExists, file_path_generator

from s3.configs import s3



def data_extraction_from_s3(s3:dict, bucket_name, file_path, columns:list=None):
    print("Extracting S3 Data")
    storage_options=storage_options_generator(s3)

    # client = client_generator(s3=s3_src)
    # print("Client")
    # if objectExists(client=client, bucket_name=bucket_name, path=file_path):
    #     full_path = file_path_generator(bucket_name, file_path)
    #     print(full_path)
    #     try:
    #         df = pd.read_parquet(
    #             path=full_path,
    #             engine="fastparquet",
    #             storage_options=storage_options,
    #             columns=columns
    #         )
    #         return df
    #     except Exception as e:
    #         print(e)
    #     # except:
    #     #     print("Error while extract file")
    #         # return pd.DataFrame()
    #         return False
    # else:
    #     print("Object Not Found")
    #     return False


    # full_path = file_path_generator(bucket_name, file_path)
    # try:
    #     df = pd.read_parquet(
    #         path=full_path,
    #         engine="fastparquet",
    #         storage_options=storage_options,
    #         columns=columns
    #     )
    #     return df
    # except ValueError as e:
    #     print(e)
    #     print("Error while extract file")
    #     return False


    full_path = file_path_generator(bucket_name, file_path)
    df = pd.read_parquet(
            path=full_path,
            engine="fastparquet",
            storage_options=storage_options,
            columns=columns
        )
    return df
    
    # full_path = file_path_generator(bucket_name, file_path)
    # df = pd.read_parquet(
    #         path=full_path,
    #         engine="fastparquet",
    #         storage_options=storage_options,
    #         columns=columns
    #     )
    # return df

# def data_extraction_from_s3_dask(file_path, storage_options, columns = None, filters=None):
#     print("Extracting S3 Data")
#     ddf = dd.read_parquet(
#         path=file_path,
#         engine="fastparquet",
#         storage_options=storage_options,
#         columns=columns,
#         filters=filters
#     )
#     return ddf
