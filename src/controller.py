from sqlalchemy.orm import Session
from uuid import UUID, uuid4
#from models import Estoque
#from schema import Item
from . import schema
from . import models


# def get_products(db: Session,skip: int = 0, limit: int = 100):
#     return db.query(models.Estoque).offset(skip).limit(limit).all()


def create_produt(db: Session, produto:schema.Produto):
    db_produtos = models.Estoque(produto=produto.produto, preco=produto.preco)
    db.add(db_produtos)
    db.commit()
    db.refresh(db_produtos)
    return db_produtos

