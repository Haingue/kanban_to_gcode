from fastapi import APIRouter, status
import logging

from web_app.jira.dto import Issue
from web_app.service.converter import add_issue_in_queue

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/service/jira/issue", status_code=status.HTTP_200_OK, response_model=list[Issue])
def load_issue ():
  logger.info("Load issue")
  return []

@router.post("/service/jira/issue", status_code=status.HTTP_201_CREATED)
def add_issue (issue: Issue):
  logger.info("New issue: %s", issue)
  add_issue_in_queue(issue)
  return issue