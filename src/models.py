#representacao do banco de dados
from sqlalchemy import Column, Integer, String, DateTime, Select, Boolean
from sqlalchemy.sql import func
from src.db import Base

class Estoque(Base):
    __tablename__ = 'estoque'
    id = Column(Integer, primary_key=True)
    produto = Column(String)
    preco = Column(Integer)
    #is_empty = Column(Boolean)
    #created_at = Column(DateTime, default=func.now())

