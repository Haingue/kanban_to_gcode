import logging
import subprocess
from kanban_to_svg.kanban import Kanban
from web_app.jira.dto import Issue
from web_app.printer.dto import KanbanGCode
from web_app.service.queue import G_CODE_QUEUE

def _generate_svg (issue: Issue):
  kanban = Kanban(issue.id, issue.title, issue.description, issue.shop, issue.estimation, issue.member)
  return kanban.generate_svg()

def _generate_gcode (svg: str):
  path = "svg_to_gcode/target/debug/svg_to_gcode.exe"
  proc = subprocess.Popen(path, stdout=subprocess.PIPE)
  output, err = proc.communicate()
  print(err)
  return output

def add_issue_in_queue (issue: Issue):
  svg = _generate_svg(issue)
  gcode = _generate_gcode(svg)
  kanban = KanbanGCode(
    id=issue.id,
    type=issue.type,
    title=issue.title,
    g_code=gcode
  )
  logging.debug("KanbanGCode: %s", kanban)
  G_CODE_QUEUE.push(kanban)
  return kanban

def is_empty ():
  return G_CODE_QUEUE.is_empty()

def pop_kanban_from_queue ():
  return G_CODE_QUEUE.pop()

def kanban_list ():
  return G_CODE_QUEUE.tolist()