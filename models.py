#representacao do banco de dados
from sqlalchemy import Column, Integer, String, DateTime, Select
from sqlalchemy.sql import func
from db import Base
from pydantic import BaseModel

class Filme(Base):
    __tablename__ = 'filmes'
    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    completed = Column(bool)
    created_at = Column(DateTime, default=func.now())

class Task(BaseModel):
   id: Optional[UUID] = None
   title: str
   description: Optional[str] = None
   completed: bool = False