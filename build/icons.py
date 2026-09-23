import json
import re
from pathlib import Path

import cairosvg
import png

ICONS_ROOT = Path(__file__).parent.parent / "icons"


def replace_color(text: str, color: str, new_color: str):
    return re.sub(rf'fill="{color}"', rf'fill="{new_color}"', text)


def create_png(bytestring: str, write_to: Path, size: int):
    _, _, rows, info = png.Reader(
        bytes=cairosvg.svg2png(bytestring=bytestring, parent_height=size, parent_width=size)
    ).asRGBA()
    with open(write_to, "wb") as fp:
        png.Writer(compression=9, **info).write(fp, rows)


def load_colors_json():
    return json.loads((ICONS_ROOT / "colors.json").read_text())


def load_icons_json():
    return json.loads((ICONS_ROOT / "icons.json").read_text())


def create_icons(icons: dict[str, object]):
    colors = load_colors_json()

    for icon_name, icon_data in icons.items():
        svg_colored = ICONS_ROOT.joinpath("svg", icon_name + ".svg").read_text()
        svg_mono = replace_color(svg_colored, ".+?", "#fff")
        color = colors.get(icon_data["color"])
        if color:
            svg_colored = replace_color(svg_colored, "#000", color)

        for size in (1, 2, 3):
            suffix = f"@{size}x.png" if size > 1 else ".png"
            create_png(
                bytestring=svg_colored,
                write_to=ICONS_ROOT.joinpath("color", icon_name + suffix),
                size=size * 16,
            )
            create_png(
                bytestring=svg_mono,
                write_to=ICONS_ROOT.joinpath("mono", icon_name + suffix),
                size=size * 16,
            )
