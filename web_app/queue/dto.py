
from pydantic import BaseModel
from web_app.printer.dto import KanbanGCode

class QueueDto(BaseModel):
    size: int
    top: str
