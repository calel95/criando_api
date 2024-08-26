from pydantic import BaseModel


class Task(BaseModel):
    id: Optional[object] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

