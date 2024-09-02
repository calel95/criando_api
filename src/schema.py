import datetime
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4




class Produto(BaseModel):
    id: Optional[UUID] = None
    produto: str | None = None
    preco: int | None = None
    created_at: datetime.datetime
    #is_empty: bool = False

    class Config:
        from_attributes = True