from fastapi import APIRouter, status
import logging

from web_app.queue.dto import QueueDto
from web_app.service.converter import load_queue_metrics

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/service/queue", status_code=status.HTTP_200_OK, response_model=QueueDto)
def get_queue_metrics ():
  logger.info("Load queue info")
  return load_queue_metrics()
