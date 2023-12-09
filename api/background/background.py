import json
from handler.worker import celery
from handler.redis import redis
from schemas.task import TaskOut

def send_task(data:TaskOut):
    try:
        redis.set(data.task_id, json.dumps(data.__dict__))
        celery.send_task(name="create_task", task_id=data.task_id, kwargs={"data": json.dumps(data.__dict__)})
    except Exception as e:
        data.task_status = "FAILED"
        redis.set(data.task_id, json.dumps(data.__dict__))
        print(e)

