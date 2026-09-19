import json
import os
import re

import cairosvg
import png

PACKAGE_ROOT = os.path.dirname(os.path.dirname(__file__))


def icons_path(*args):
    return os.path.join(PACKAGE_ROOT, "icons", *args)


def replace_color(text, color, new_color):
    return re.sub(rf'fill="{color}"', rf'fill="{new_color}"', text)


def create_png(bytestring, write_to, size):
    _, _, rows, info = png.Reader(
        bytes=cairosvg.svg2png(bytestring=bytestring, parent_height=size, parent_width=size)
    ).asRGBA()
    with open(write_to, "wb") as fp:
        png.Writer(compression=9, **info).write(fp, rows)


def create_icons(icons):
    with open(icons_path("colors.json")) as fp:
        colors = json.load(fp)

    for icon_name, icon_data in icons.items():
        with open(icons_path("svg", icon_name + ".svg")) as fp:
            svg_colored = fp.read()
            svg_mono = replace_color(svg_colored, ".+?", "#fff")
            color = colors.get(icon_data["color"])
            if color:
                svg_colored = replace_color(svg_colored, "#000", color)

        for size in (1, 2, 3):
            suffix = f"@{size}x.png" if size > 1 else ".png"
            create_png(
                bytestring=svg_colored,
                write_to=icons_path("color", icon_name + suffix),
                size=size * 16,
            )
            create_png(
                bytestring=svg_mono,
                write_to=icons_path("mono", icon_name + suffix),
                size=size * 16,
            )
