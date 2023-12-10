import cairosvg
import json
import os
import png
import re
import subprocess


PACKAGE_ROOT = os.path.dirname(os.path.dirname(__file__))


def icons_path(*args):
    return os.path.join(PACKAGE_ROOT, "icons", *args)


def replace_color(text, color, new_color):
    return re.sub(r'fill="{0}"'.format(color), r'fill="{0}"'.format(new_color), text)


def create_png(bytestring, write_to, size):
    _, _, rows, info = png.Reader(
        bytes=cairosvg.svg2png(
            bytestring=bytestring, parent_height=size, parent_width=size
        )
    ).asRGBA()
    with open(write_to, "wb") as fp:
        png.Writer(compression=9, **info).write(fp, rows)


def create_icons(icons):
    with open(icons_path("colors.json")) as fp:
        colors = json.load(fp)

    for icon_name, icon_data in icons.items():
        with open(icons_path("svg", icon_name + ".svg")) as fp:
            svg_multi = fp.read()
            svg_mono = replace_color(svg_multi, ".+?", "#fff")
            color = colors.get(icon_data["color"])
            if color:
                svg_multi = replace_color(svg_multi, "#000", color)

        for size in (1, 2, 3):
            suffix = "@{}x.png".format(size) if size > 1 else ".png"
            create_png(
                bytestring=svg_multi,
                write_to=icons_path("multi", icon_name + suffix),
                size=size * 16,
            )
            create_png(
                bytestring=svg_mono,
                write_to=icons_path("single", icon_name + suffix),
                size=size * 16,
            )

    # recreate icons overlay
    # note: requires `subl` to be registered on $PATH
    try:
        subprocess.call(["subl", "--command", "afi_revert"])
    except:
        pass
