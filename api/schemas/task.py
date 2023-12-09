from pydantic import BaseModel
from typing import Optional

class TaskIn(BaseModel):
    type: int

    class Config:
        schema_extra = {"example" : {"type":10}}

class TaskOut(BaseModel):
    task_id: str
    task_status: str
    multiplier: int
    sleep_time: Optional[int] = None
    task_result: Optional[str] = None
