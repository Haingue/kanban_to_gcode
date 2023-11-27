
from pydantic import BaseModel


class Issue(BaseModel):
    id: str
    type: str
    title: str
    description: str
    shop: str
    estimation: float
    member: str
