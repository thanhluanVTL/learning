import time
from pandas_handler import PandasHandler

pandas_handler = PandasHandler()


path="s3://test/get_all_cust*.parquet"

start_time = time.time()
df = pandas_handler.read_parquet_s3(path=path, columns=["c_customer_code"])

print(df)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))