
import ezdxf
from ezdxf import colors
from ezdxf.addons.drawing import Frontend, RenderContext, svg, layout
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

  def create_doc (self):
    doc = ezdxf.new(dxfversion="R2010")
    doc.layers.add("TEXTLAYER", color=colors.BLACK)
    msp = doc.modelspace()
    self.draw(msp)
    return doc

  def create_svg (self, doc):
    msp = doc.modelspace()
    # 1. create the render context
    context = RenderContext(doc)
    # 2. create the backend
    backend = svg.SVGBackend()
    # 3. create the frontend
    frontend = Frontend(context, backend)
    # 4. draw the modelspace
    frontend.draw_layout(msp)
    # 5. create an kanban foramt  layout [10.5, 6.8]
    page = layout.Page(0,0, layout.Units.mm, margins=layout.Margins(2, 2, 2, 10))
    # 6. get the SVG rendering as string - this step is backend dependent
    svg_string = backend.get_string(
      page,
      settings=layout.Settings(scale=1, fit_page=False)
      )
    return svg_string

  def generate_svg (self):
    doc = self.create_doc()
    svg = self.create_svg(doc)
    return svg