import time
import dask.dataframe as dd
from dask.distributed import Client, LocalCluster, Future
from dask_handler import DaskHandler


client = Client('192.168.1.92:8786', timeout='2s')
# client = Client('localhost:8786', timeout='2s')

dask_handler = DaskHandler()


path="s3://test/get_all_cust.parquet"

start_time = time.time()
df = dask_handler.read_parquet_s3(path=path, columns=["c_customer_code"])

print(df)
# print(df.compute())
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))

