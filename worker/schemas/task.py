from pydantic import BaseModel
from typing import Optional

class TaskIn(BaseModel):
    type: int

    class Config:
        schema_extra = {"example" : {"type":10}}

class TaskOut(BaseModel):
    task_id: str
    task_status: str
    task_type: int
    task_result: Optional[int] = None
