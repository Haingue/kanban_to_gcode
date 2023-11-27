from fastapi import APIRouter, HTTPException, status
import logging

from web_app.printer.dto import KanbanGCode
from web_app.service.converter import is_empty, kanban_list, pop_kanban_from_queue

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/service/printer/kanban", status_code=status.HTTP_200_OK)
def load_kanban_queue ():
  logger.info("Load queue")
  list = kanban_list()
  return list

@router.get("/service/printer/kanban/pop", status_code=status.HTTP_200_OK, response_model=KanbanGCode)
def pop_kanban ():
  logger.info("Pop kanban")
  if is_empty() :
    raise HTTPException(status_code=204, detail="Queue is empty")
  kanban = pop_kanban_from_queue()
  return kanban
