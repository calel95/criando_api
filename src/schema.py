from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4




class Produto(BaseModel):
    id: Optional[UUID] = None
    produto: str | None = None
    preco: int | None = None
    #is_empty: bool = False

    class Config:
        orm_mode = True
