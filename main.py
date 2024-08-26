from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
#from schema import Task

app = FastAPI()


class Task(BaseModel):
   id: Optional[object] = None
   title: str
   description: Optional[str] = None
   completed: bool = False
                 
tasks = []

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task

@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return tasks
