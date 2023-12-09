import json, uuid
from fastapi import APIRouter, BackgroundTasks, Body, HTTPException
from fastapi.responses import JSONResponse
from celery.result import AsyncResult

from handler.worker import celery
from handler.redis import redis

from schemas.task import TaskIn, TaskOut

from starlette.status import (HTTP_400_BAD_REQUEST)

from background.background import send_task



router = APIRouter(prefix="", tags=["Task Manager"])

# @router.post("/tasks", status_code=201)
# def run_task(payload = Body(...)):
#     task_type = payload["type"]
#     # task = create_task.delay(int(task_type))
#     task = celery.send_task(name="create_task", kwargs={'task_type': task_type})
#     return JSONResponse({"task_id": task.id})


# @router.get("/tasksss/{task_id}")
# def get_status(task_id):
#     task_result = AsyncResult(task_id)
#     result = {
#         "task_id": task_id,
#         "task_status": task_result.status,
#         "task_result": task_result.result
#     }
#     return JSONResponse(result)



@router.post("/tasks", status_code=201, response_model=TaskOut)
def run_task(payload:TaskIn, background_task:BackgroundTasks):
    task_id = str(uuid.uuid4())
    multiplier = int(json.loads(payload.json())["type"])
    data = TaskOut(task_id=task_id, task_status="PENDING", multiplier=multiplier)
    background_task.add_task(send_task, data)

    return data

@router.get("/tasks/{task_id}", response_model=TaskOut)
def get_status(task_id:str):
    data = redis.get(task_id)
    if data == None:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="task_id not found!")
    status = json.loads(data)
    return status