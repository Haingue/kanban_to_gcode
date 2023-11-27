
from pydantic import BaseModel


class KanbanGCode(BaseModel):
    id: str
    type: str
    title: str
    g_code: str
