import datetime
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4




class Produto(BaseModel):
    produto: str | None = None
    preco: int | None = None

    class Config:
        from_attributes = True

class ProdutoGet(Produto):
    created_at: datetime.datetime
    id: Optional[UUID] = None

    class Config:
        from_attributes = True