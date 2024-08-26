#representacao do banco de dados
from sqlalchemy import Column, Integer, String, DateTime, Select
from sqlalchemy.sql import func
from db import Base

class Filme(Base):
    __tablename__ = 'filmes'
    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    completed = Column(bool)
    created_at = Column(DateTime, default=func.now())

    id: Optional[object] = None
    title: str
    description: Optional[str] = None
    completed: bool = False