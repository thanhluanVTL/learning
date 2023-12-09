import os, time, json, random
from celery import Celery
from utils.utils import getenv

from schemas.task import TaskOut


celery = Celery(__name__)
# celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
# celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")
celery.conf.broker_url = getenv("CELERY_BROKER_URL")
celery.conf.result_backend = getenv("CELERY_RESULT_BACKEND")


# @celery.task(name="create_task")
# def create_task(task_type):
#     time.sleep(int(task_type) * 10)
#     return {
#         "task_type" : task_type,
#         "sleep" : int(task_type) * 10
#         }



from redis import Redis

redis = Redis(host="redis", port="6379", db=0)


# @celery.task(name="create_task")
# def create_task(data:bytes):
#     data = json.loads(data)
#     task_id = data["task_id"]
    
#     try:
#         task_type = data["task_type"]
#         task_result = int(task_type) * random.randint(5,10)
#         data["task_result"] = task_result
#         data["task_status"] = "SUCCESS"

#         time.sleep(task_result)
#         redis.set(task_id, json.dumps(data))
#         return data
#     except Exception as e:
#         data["task_status"] = "FAILED"
#         redis.set(task_id, json.dumps(data))
#         print(e)
#         return data



from helper.helper import dict_to_json_s3, id_generator

@celery.task(name="create_task")
def create_task(data:bytes):
    data = json.loads(data)
    task_id = data["task_id"]
    
    try:
        multiplier = data["multiplier"]
        sleep_time = int(multiplier) * random.randint(5,10)
        data["sleep_time"] = sleep_time
        data["task_status"] = "SUCCESS"

        dict_ = {
            "id": id_generator(),
            "task_id" : task_id,
            "multiplier" : multiplier,
            "sleep_time" : sleep_time,
            "task_status" : "SUCCESS"
        }
        data["task_result"] = dict_to_json_s3(task_id=task_id, data=dict_)

        time.sleep(sleep_time)

        redis.set(task_id, json.dumps(data))
        return data
    except Exception as e:
        data["task_status"] = "FAILED"
        redis.set(task_id, json.dumps(data))
        print(e)
        return data
