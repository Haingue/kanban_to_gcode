from collections import deque

from web_app.printer.dto import KanbanGCode

class GCodeQueue:
  def __init__(self):
    self.queue = deque()

  def push (self, kanban: KanbanGCode):
    self.queue.append(kanban)
    return self.queue
    
  def pop (self):
    return self.queue.popleft()
  
  def is_empty (self):
    return len(self.queue) == 0
  
  def len (self):
    return len(self.queue)
  
  def tolist (self):
    return list(self.queue)
  
  def peek (self):
    return self.queue[0]
  
G_CODE_QUEUE = GCodeQueue()