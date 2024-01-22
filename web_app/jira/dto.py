from typing import List
from pydantic import BaseModel

class Assignee(BaseModel):
    displayName: str

class Status(BaseModel):
    name: str
    description: str

class Shop(BaseModel):
    name: str
    description: str

class TypeOfActivity(BaseModel):
    name: str
    description: str

class Fields(BaseModel):
    assignee: Assignee
    summary: str
    shop: Shop
    typeOfActivity: TypeOfActivity
    timeestimate: str
    status: Status

class Issue(BaseModel):
    id: str
    key: str
    fields: Fields