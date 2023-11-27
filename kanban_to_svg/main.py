import kanban
import ezdxf
from ezdxf import colors
from ezdxf.addons.drawing import Frontend, RenderContext, svg, layout

def export(doc, path):
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
    if (path != None):
      with open(path, "wt", encoding="utf8") as fp:
          fp.write(svg_string)
    return svg_string

def draw_kanban (kanban:kanban.Kanban):
  doc = ezdxf.new(dxfversion="R2010")
  doc.layers.add("TEXTLAYER", color=colors.BLACK)
  msp = doc.modelspace()
  kanban.draw(msp)
  return doc

# Load kanban
kanban = kanban.Kanban("TIS-180", "[Title]", "[Description]", "IS", "5", "FHA")
# Draw Kanban
doc = draw_kanban(kanban)
# Export to SVG
export(doc, "resources/test.svg")

# exemple_svg("resources/test.svg")