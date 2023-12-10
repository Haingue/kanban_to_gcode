
from pydantic import BaseModel
from datetime import datetime

class KanbanGCode(BaseModel):
    id: str
    type: str
    title: str
    creationDate: datetime
    g_code: str
