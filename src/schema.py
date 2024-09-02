import datetime
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4




class Produto(BaseModel):
    id: Optional[UUID] = None
    produto: str | None = None
    preco: int | None = None

    class Config:
        from_attributes = True

class ProdutoGet(Produto):
    created_at: datetime.datetime

    class Config:
        from_attributes = True