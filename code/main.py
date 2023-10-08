import dask.dataframe as dd
from dask.distributed import Client, LocalCluster, Future
import json

client = Client('localhost:8786', timeout='2s')
# client = Client('tcp://localhost:8786', timeout='2s')
client

# try:
#     client = Client('tcp://localhost:8786', timeout='2s')
# except OSError:
#     cluster = LocalCluster(scheduler_port=8786)
#     client = Client(cluster)
# client

path = r"C:\Users\Thanh Luan\Documents\Code\dask\code\t_cust_customer.parquet"

if __name__ == '__main__':

    ddf = dd.read_parquet(
        path
    )

    print(ddf)
    # print(ddf.compute())

    # ddf.groupby(ddf.c_marketing_id).value.mean().compute()
    # ddf.groupby(ddf.c_marketing_id).compute()

    # future: Future = client.compute(ddf)

    # print(future)

    # parsed = json.loads(future.to_json(orient="records"))

    # print(parsed)

    print(client.compute(ddf).to_frame())