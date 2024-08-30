from sqlalchemy.orm import Session
from uuid import UUID, uuid4
#from models import Estoque
#from schema import Item
from . import schema
from . import models

def get_one_product(db: Session, produto_id: str):
    return db.query(models.Estoque).filter(models.Estoque.id == produto_id).first()

def get_products(db: Session,skip: int = 0, limit: int = 100):
    return db.query(models.Estoque).offset(skip).limit(limit).all()


def create_produt(db: Session, produto:schema.Produto):
    pk = str(uuid4())
    db_produtos = models.Estoque(id=pk, produto=produto.produto, preco=produto.preco)
    db.add(db_produtos)
    db.commit()
    db.refresh(db_produtos)
    return db_produtos

def update_product(db: Session, produto_id: str, produto: schema.Produto):
    db_produto =  db.query(models.Estoque).filter(models.Estoque.id == produto_id).first()
    if db_produto is None:
        return None  # ou você pode levantar uma exceção aqui  
    db_produto.produto = produto.produto
    db_produto.preco = produto.preco

    db.commit()
    db.refresh(db_produto)
    return db_produto


