import logging
import os
import subprocess
from kanban_to_svg.kanban import Kanban
from web_app.jira.dto import Issue
from web_app.printer.dto import KanbanGCode
from web_app.queue.dto import QueueDto
from web_app.service.queue import G_CODE_QUEUE
from datetime import datetime

logger = logging.getLogger(__name__)

def _generate_svg (issue: Issue):
  kanban = Kanban(issue.key, issue.fields.summary, issue.fields.description, issue.fields.shop.name, issue.fields.timeestimate, issue.fields.assignee.displayName)
  return kanban.generate_svg()

def _generate_gcode (svg: str):
  rust_program = "svg_to_gcode"
  logger.info("Svg: %s" % svg)
  env = os.environ.copy()
  rust_process = subprocess.Popen([rust_program, "--stream"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=env)
  rust_stdin = rust_process.stdin
  rust_stdin.write(svg.encode())
  rust_stdin.close()

  err = rust_process.stderr
  logger.debug(err)
  logger.debug(rust_process.returncode)
  gcode = rust_process.stdout.read()
  logger.debug(gcode)
  return gcode

def add_issue_in_queue (issue: Issue):
  svg = _generate_svg(issue)
  gcode = _generate_gcode(svg)
  kanban = KanbanGCode(
    id=issue.key,
    type=issue.fields.issuetype.name,
    title=issue.fields.summary,
    g_code=gcode,
    creationDate=datetime.now()
  )
  logger.debug("KanbanGCode: %s", kanban)
  G_CODE_QUEUE.push(kanban)
  return kanban

def is_empty ():
  return G_CODE_QUEUE.is_empty()

def length ():
  return G_CODE_QUEUE.len()

def pop_kanban_from_queue ():
  return G_CODE_QUEUE.pop()

def kanban_list ():
  return G_CODE_QUEUE.tolist()

def load_queue_metrics ():
  size = 0
  top = ""
  if not G_CODE_QUEUE.is_empty():
    size = G_CODE_QUEUE.len()
    top=G_CODE_QUEUE.peek().id
  return QueueDto(size=size, top=top)