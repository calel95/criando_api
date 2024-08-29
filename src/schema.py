from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4




class Produto(BaseModel):
    id: Optional[UUID] = None
    produto: str
    preco: int
    #is_empty: bool = False

    class Config:
        orm_mode = True
