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
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# Dependency
def get_db():
    with SessionLocal() as db:
        yield db

@app.post("/produtos/", response_model=schema.Produto)
def create_product(produto: schema.Produto, db: Session = Depends(get_db)):
    db_produto = controller.create_produt(db=db, produto=produto)   
    return db_produto
    # db_produtos = controller.create_produt(db, product=produto.product)
    # if db_produtos:
    #     raise HTTPException(status_code=400, detail="Produto já cadastrado!")
    # return controller.create_produt(db=db, product=produto)

# @app.get("/produtos/", response_model=schema.ProdutoList)
# def read_products(db: Session = Depends(get_db)):
#     produtos = controller.get_products(db)
#     return produtos



























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
