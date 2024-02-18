from fastapi import APIRouter, status
import logging

from pyparsing import Any, Dict

from web_app.jira.dto import Assignee, Fields, Issue, IssueType, Shop, Status
from web_app.service.converter import add_issue_in_queue

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/service/jira/issue", status_code=status.HTTP_201_CREATED)
def add_issue (data: dict):
  assignee = Assignee()
  try:
    assignee.displayName=data['fields']['assignee']['displayName']
  except: None
  status = Status()
  try:
    status.name = data['fields']['status']['name']
  except: None
  try:
    status.description = data['fields']['status']['description']
  except: None
  try:
    status.iconUrl = data['fields']['status']['iconUrl']
  except: None
  issuetype = IssueType()
  try:
    issuetype.name = data['fields']['issuetype']['name']
  except: None
  try:
    issuetype.namedValue = data['fields']['issuetype']['namedValue']
  except: None
  try:
    issuetype.description = data['fields']['issuetype']['description']
  except: None
  try:
    issuetype.iconUrl = data['fields']['issuetype']['iconUrl']
  except: None
  
  shop = Shop()
  try:
    shop.name=data['fields']['customfield_17537'][0]['value']
  except: None
  
  fields = Fields()
  fields.assignee=assignee
  fields.shop=shop
  fields.issuetype=issuetype
  fields.status=status
  try:
    fields.summary=data['fields']['summary']
  except: None
  try:
    fields.description=data['fields']['description']
  except: None
  try:
    fields.timeestimate=data['fields']['timeestimate']
  except: None
  
  issue = Issue()
  try:
    issue.id = data['id']
  except: None
  try:
    issue.key = data['key']
  except: None
  issue.fields = fields
  logger.info("New issue: %s", issue)
  add_issue_in_queue(issue)
  return issue