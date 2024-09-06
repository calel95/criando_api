import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from uuid import UUID, uuid4




class Produto(BaseModel):
    produto: str | None = None
    preco: int | None = None

    # class Config:
    #     from_attributes = True
    model_config = ConfigDict(from_attributes=True)

class ProdutoGet(Produto):
    created_at: datetime.datetime
    id: Optional[UUID] = None
    updated: bool | None = None
    update_date: datetime.datetime | None

    # class Config:
    #     from_attributes = True
    model_config = ConfigDict(from_attributes=True)