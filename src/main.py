from fastapi import FastAPI, HTTPException, Depends
from uuid import UUID, uuid4
from sqlalchemy.orm import Session
from . import schema
from . import models
from . import controller
from .db import SessionLocal, engine

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


@app.get("/produtos/", response_model=list[schema.ProdutoGet])
def read_products(db: Session = Depends(get_db)):
    produtos = controller.get_products(db)
    return produtos

@app.get("/produtos/{produto_id}", response_model=schema.ProdutoGet)
def read_one_product(produto_id: str, db: Session = Depends(get_db)):
    db_produto = controller.get_one_product(db=db, produto_id=produto_id)
    return db_produto

@app.put("/produtos/{produto_id}", response_model=schema.Produto)
def update_one_product(produto_id:str, produto:schema.Produto, db: Session = Depends(get_db)):
    update_produto = controller.update_product(db=db, produto_id=produto_id,produto=produto)
    return update_produto

@app.delete("/produtos/{produto_id}", response_model=schema.Produto)
def delete_one_product(produto_id: str, db: Session = Depends(get_db)):
    product_deleted = controller.delete_product(db=db,produto_id=produto_id)
    if product_deleted is None:
        raise HTTPException(status_code=404, detail="Task nao encontrada!!")
    return product_deleted
