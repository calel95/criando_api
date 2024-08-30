from fastapi import FastAPI, HTTPException, Depends
from uuid import UUID, uuid4
from sqlalchemy.orm import Session
from . import schema
from . import models
from . import controller
from src.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    with SessionLocal() as db:
        yield db

@app.post("/produtos/", response_model=schema.Produto)
def create_product(produto: schema.Produto, db: Session = Depends(get_db)):
    db_produto = controller.create_produt(db=db, produto=produto)   
    return db_produto


@app.get("/produtos/", response_model=list[schema.Produto])
def read_products(db: Session = Depends(get_db)):
    produtos = controller.get_products(db)
    return produtos

@app.get("/produtos/{produto_id}", response_model=schema.Produto)
def read_one_product(produto_id: str, db: Session = Depends(get_db)):
    db_produto = controller.get_one_product(db=db, produto_id=produto_id)
    return db_produto

@app.put("/produtos/{produto_id}", response_model=schema.Produto)
def update_one_product(produto_id:str, produto:schema.Produto, db: Session = Depends(get_db)):
    update_produto = controller.update_product(db=db, produto_id=produto_id,produto=produto)
    return update_produto



























# @app.post("/tasks/", response_model=Task)
# def create_task(task: Task):
#     task.id = uuid4()
#     tasks.append(task)
#     return task

# @app.get("/tasks/", response_model=List[Task])
# def read_tasks():
#     return tasks

# @app.get("/tasks/{task_id}", response_model=Task)
# def read_task(task_id: UUID):
#     for task in tasks:
#         if task.id == task_id:
#             return task
#     raise HTTPException(status_code=404, detail="Task nao encontrada!!")

# @app.put("/tasks/{task_id}", response_model=Task)
# def update_task(task_id: UUID, task_update: Task):
#     for idx, task in enumerate(tasks):
#         if task.id == task_id:
#             update_task = task.copy(update=task_update.model_dump(exclude_unset=True))
#             tasks[idx] = update_task
#             return update_task
#     raise HTTPException(status_code=404, detail="task nao encontrada!!")


# @app.delete("/tasks/{task_id}", response_model=Task)
# def delete_task(task_id: UUID):
#     for idx, task in enumerate(tasks):
#         if task.id == task_id:
#             return tasks.pop(idx)
#     raise HTTPException(status_code=404, detail="task nao encontrada!!")
