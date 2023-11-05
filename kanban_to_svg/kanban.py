from ezdxf.layouts import Modelspace

class Kanban:
  def __init__(self, id, title, description, shop, estimation, member) -> None:
    self.id = id
    self.title = title
    self.description = description
    self.shop = shop
    self.estimation = estimation
    self.member = member

  def draw_id (self, model:Modelspace) -> None:
    model.add_text(
      self.id,
      dxfattribs={
          "layer": "TEXTLAYER"
      }).set_placement((0, 0))

  def draw_title (self, model:Modelspace) -> None:
    model.add_text(
    self.title,
    dxfattribs={
        "layer": "TEXTLAYER"
    }).set_placement((40, 50))

  def draw_description (self, model:Modelspace) -> None:
    model.add_mtext(
      self.description,
      dxfattribs={
          "layer": "TEXTLAYER"
      }).set_location((40, 45))

  def draw_shop (self, model:Modelspace) -> None:
    model.add_text(
    self.shop,
    dxfattribs={
        "layer": "TEXTLAYER"
    }).set_placement((100, 60))

  def draw_estimation (self, model:Modelspace) -> None:
    model.add_text(
    self.estimation,
    dxfattribs={
        "layer": "TEXTLAYER"
    }).set_placement((100, 0))

  def draw_member (self, model:Modelspace) -> None:
    model.add_text(
      self.member,
      dxfattribs={
          "layer": "TEXTLAYER"
      }).set_placement((0, 60))

  def draw (self, model:Modelspace) -> None:
    self.draw_id(model)
    self.draw_title(model)
    self.draw_description(model)
    self.draw_shop(model)
    self.draw_estimation(model)
    self.draw_member(model)