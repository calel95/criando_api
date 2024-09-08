#representacao do banco de dados
from sqlalchemy import Column, Integer, String, DateTime, Select, Boolean
from sqlalchemy.sql import func
from .db import Base

class Estoque(Base):
    __tablename__ = 'estoque'
    id = Column(String, primary_key=True)
    produto = Column(String)
    preco = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated = Column(Boolean, default=False)
    update_date = Column(DateTime)