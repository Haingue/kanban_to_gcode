from typing import Union
from fastapi import FastAPI

from web_app.jira.app import router as jira_router
from web_app.printer.app import router as printer_router

app = FastAPI()
app.include_router(jira_router)
app.include_router(printer_router)

@app.get("/actuator/status")
def get_status():
    return "UP"