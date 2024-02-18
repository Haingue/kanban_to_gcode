from typing import List
from pydantic import BaseModel

class Assignee():
    displayName: str

class Status():
    name: str
    description: str
    iconUrl: str

class Shop():
    name: str

class IssueType():
    name: str
    namedValue: str
    description: str
    iconUrl: str

class Fields():
    assignee: Assignee
    summary: str
    description: str
    shop: Shop
    issuetype: IssueType
    timeestimate: str
    status: Status

class Issue():
    id: str
    key: str
    fields: Fields