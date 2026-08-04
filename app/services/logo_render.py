# import copy
# import math
# from pathlib import Path
# import xml.etree.ElementTree as ET

# from app.models.logo import LogoConfig
# from app.services.logo_asset_service import LogoAssetService
# from app.utils.vne_config import SVG_NS


# ET.register_namespace("", SVG_NS) 
# GOLD = "#D4AF37"


# def _qn(tag: str) -> str:
#     return f"{{{SVG_NS}}}{tag}"


# def _el(tag: str, attrib: dict) -> ET.Element:
#     return ET.Element(_qn(tag), {k: str(v) for k, v in attrib.items()})


# class LogoRender:
#     WIDTH = 512
#     HEIGHT = 512

#     def __init__(self, asset_service: LogoAssetService):
#         self.asset_service = asset_service


#     def _load_group(self, path: Path) -> ET.Element:
#         root = ET.parse(path).getroot()
#         g = root.find(_qn("g"))
#         if g is None:
#             raise ValueError(f"{path} has no top-level <g>")
#         return g

#     def _colorized(self, group: ET.Element, color: str) -> ET.Element:
#         group = copy.deepcopy(group)
#         for node in group.iter():
#             if node.attrib.get("fill") in ("black", "#000", "#000000"):
#                 node.set("fill", color)
#         return group


#     def _pattern_shapes(self, pattern: str, color: str) -> list[ET.Element]:
#         w, h = self.WIDTH, self.HEIGHT
#         if pattern == "solid":
#             return []
#         if pattern == "split":
#             return [_el("rect", {"x": w / 2, "y": 0, "width": w / 2, "height": h, "fill": color})]
#         if pattern == "stripes":
#             band = h / 8
#             return [
#                 _el("rect", {"x": 0, "y": i * band, "width": w, "height": band, "fill": color})
#                 for i in range(0, 8, 2)
#             ]
#         if pattern == "diagonal":
#             pts = f"0,0 {w},0 {w},{h*0.3:.0f} 0,{h*0.7:.0f}"
#             return [_el("polygon", {"points": pts, "fill": color})]
#         if pattern == "chevrons":
#             step = h / 6
#             shapes = []
#             for i in range(6):
#                 y = i * step
#                 pts = (
#                     f"0,{y:.0f} {w/2:.0f},{y+step*0.5:.0f} {w:.0f},{y:.0f} "
#                     f"{w:.0f},{y+step*0.3:.0f} {w/2:.0f},{y+step*0.8:.0f} 0,{y+step*0.3:.0f}"
#                 )
#                 shapes.append(_el("polygon", {"points": pts, "fill": color}))
#             return shapes
#         return []


#     def _border_group(self, shield: ET.Element, border_style: str, accent_color: str) -> ET.Element:
#         outline = copy.deepcopy(shield)
#         color = GOLD if border_style == "gold" else accent_color
#         width = {"thin": 4, "bold": 12, "double": 8, "gold": 10}.get(border_style, 4)
#         for node in outline.iter():
#             if node.tag == _qn("path"):
#                 node.set("fill", "none")
#                 node.set("stroke", color)
#                 node.set("stroke-width", str(width))
#         if border_style == "double":
#             inner = copy.deepcopy(outline)
#             for node in inner.iter():
#                 if node.tag == _qn("path"):
#                     node.set("stroke-width", "3")
#                     node.set("stroke", accent_color)
#             wrapper = _el("g", {})
#             wrapper.append(outline)
#             wrapper.append(inner)
#             return wrapper
#         return outline


#     def _star_points(self, cx: float, cy: float, outer_r: float, inner_r: float) -> str:
#         pts, angle = [], -math.pi / 2
#         for i in range(10):
#             r = outer_r if i % 2 == 0 else inner_r
#             pts.append(f"{cx + r*math.cos(angle):.1f},{cy + r*math.sin(angle):.1f}")
#             angle += math.pi / 5
#         return " ".join(pts)

#     def _stars_group(self, count: int, color: str) -> ET.Element:
#         count = min(count, 5)
#         group = _el("g", {})
#         spacing = 26
#         start_x = self.WIDTH / 2 - (count - 1) * spacing / 2
#         for i in range(count):
#             cx = start_x + i * spacing
#             pts = self._star_points(cx, 380, 10, 4)
#             group.append(_el("polygon", {"points": pts, "fill": color}))
#         return group


#     def render(self, config: LogoConfig) -> ET.Element:
#         root = _el("svg", {
#             "width": self.WIDTH, "height": self.HEIGHT,
#             "viewBox": f"0 0 {self.WIDTH} {self.HEIGHT}",
#         })

#         raw_shield = self._load_group(self.asset_service.shield_dir / config.shield_file)

#         defs = _el("defs", {})
#         clip = _el("clipPath", {"id": "shieldClip"})
#         clip.append(copy.deepcopy(raw_shield))
#         defs.append(clip)
#         root.append(defs)

#         shield = self._colorized(raw_shield, config.primary_color)
#         root.append(shield)

#         pattern_shapes = self._pattern_shapes(config.pattern, config.secondary_color)
#         if pattern_shapes:
#             pattern_group = _el("g", {"clip-path": "url(#shieldClip)"})
#             for shape in pattern_shapes:
#                 pattern_group.append(shape)
#             root.append(pattern_group)

#         if config.mascot_file:
#             raw_mascot = self._load_group(self.asset_service.mascot_dir / config.mascot_file)
#             mascot = self._colorized(raw_mascot, config.accent_color)
#             wrapper = _el("g", {"transform": "translate(128,60) scale(0.5)"})
#             wrapper.append(mascot)
#             root.append(wrapper)

#         root.append(self._border_group(raw_shield, config.border_style, config.accent_color))

#         if config.stars:
#             root.append(self._stars_group(config.stars, config.accent_color))

#         initials = _el("text", {
#             "x": "50%", "y": "82%", "text-anchor": "middle",
#             "font-size": 46, "font-family": "Arial", "font-weight": "bold",
#             "fill": config.secondary_color,
#         })
#         initials.text = config.initials
#         root.append(initials)

#         year = _el("text", {
#             "x": "50%", "y": "91%", "text-anchor": "middle",
#             "font-size": 20, "font-family": "Arial",
#             "fill": config.secondary_color,
#         })
#         year.text = str(config.founded_year)
#         root.append(year)

#         return root

#     def save(self, config: LogoConfig, output: str | Path) -> None:
#         root = self.render(config)
#         ET.ElementTree(root).write(str(output), xml_declaration=True, encoding="utf-8")