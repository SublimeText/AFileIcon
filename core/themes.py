import json
from itertools import chain
from pathlib import Path

import sublime

from .utils.logging import dump, log


def patch(settings: dict[str, sublime.Value], overwrite: bool = False, on_demand: bool = False):
    theme_packages = _installed_themes()
    themes = {theme for theme in chain(*theme_packages.values())}
    try:
        if on_demand and patch.themes == themes:
            return
    except AttributeError:
        pass
    patch.themes = themes

    supported = _customizable_themes()

    package_name, *_ = __spec__.parent.split(".")
    patch_root = Path(sublime.cache_path(), package_name)
    patch_root.mkdir(parents=True, exist_ok=True)

    general_patch = _create_general_patch(settings)
    specific_patch = _create_specific_patch(settings)

    patched = set()

    if theme_packages:
        log("Patching themes")
        for package, themes in theme_packages.items():
            patched.update(
                _patch_themes(
                    themes,
                    patch_root,
                    specific_patch if package in supported else general_patch,
                    overwrite,
                )
            )
    else:
        log("No themes to patch!")

    log("Removing obsolete theme patches")
    for file in patch_root.iterdir():
        if file.name.endswith(".sublime-theme") and file.name not in patched:
            try:
                file.unlink()
                dump(file.name)
            except OSError:
                pass


def _customizable_themes():
    log("Getting the list of theme packages with customization support")

    customizable = set()
    for res in sublime.find_resources(".supports-a-file-icon-customization"):
        if not res.startswith("Packages/"):
            continue

        _, package, _ = res.split("/")
        customizable.add(package)

    dump(customizable)
    return customizable


def _installed_themes():
    log("Getting installed themes")

    found_themes = set()
    theme_packages = {}

    for res in sublime.find_resources("*.sublime-theme"):
        if not res.startswith("Packages/"):
            continue

        _, package, *_, theme = res.split("/")
        if theme not in found_themes:
            found_themes.add(theme)
            theme_packages.setdefault(package, []).append(theme)

    dump(theme_packages)
    return theme_packages


def _patch_themes(themes: set[str], dest: Path, text: str, overwrite: bool) -> set[str]:
    patched = set()
    mode = "w" if overwrite else "x"
    for theme in themes:
        try:
            filename = dest / theme
            patched.add(filename.name)
            with open(filename, mode) as t:
                t.write(text)
        except FileExistsError:
            log(f"Ignored `{theme}`")
        except Exception as exc:
            log(f"Error patching `{theme}`")
            dump(exc)
        else:
            log(f"Patched `{theme}`")
    return patched


def _create_general_patch(settings: dict[str, sublime.Value]) -> str:
    log("Preparing general patch")
    theme_content = []

    row_padding = settings.get("row_padding")
    if row_padding:
        theme_content.append({"class": "sidebar_tree", "row_padding": row_padding})

    color = settings.get("color")
    opacity = settings.get("opacity")
    icon = _patch_icon(None, color, opacity)

    size = settings.get("size")
    if size:
        icon["content_margin"] = [size, size]

    theme_content.append(icon)

    color = settings.get("color_on_hover")
    opacity = settings.get("opacity_on_hover")
    if color or opacity:
        theme_content.append(_patch_icon("hover", color, opacity))

    color = settings.get("color_on_select")
    opacity = settings.get("opacity_on_select")
    if color or opacity:
        theme_content.append(_patch_icon("selected", color, opacity))

    dump(theme_content)
    return json.dumps(theme_content)


def _create_specific_patch(settings: dict[str, sublime.Value]) -> str:
    log("Preparing specific patch")
    theme_content = []

    row_padding = settings.get("row_padding")
    if row_padding:
        theme_content.append({"class": "sidebar_tree", "row_padding": row_padding})

    color = settings.get("color")
    icon = _patch_icon(None, color)

    size = settings.get("size")
    if size:
        icon["content_margin"] = [size, size]

    theme_content.append(icon)

    if color:
        color_on_hover = settings.get("color_on_hover")
        if color_on_hover:
            theme_content.append(_patch_icon("hover", color_on_hover))

        color_on_select = settings.get("color_on_select")
        if color_on_select:
            theme_content.append(_patch_icon("selected", color_on_select))

    dump(theme_content)
    return json.dumps(theme_content)


def _patch_icon(
    attrib: str | None, color: sublime.Value = None, opacity: sublime.Value = None
) -> sublime.Value:
    """Built an icon theme rule

    :attrib:
        The tree row's state attribute the returned rule applies to.
    :color:
        The color to tint the icon with.
        It is always required to override any theme settings. The default value of
        `none` removes any tinting specified by a theme to display colored icons.
    :opacity:
        If specified overwrites theme's opacity setting.
    """
    icon = {"class": "icon_file_type", "layer0.tint": color}
    if attrib:
        icon["parents"] = [{"class": "tree_row", "attributes": [attrib]}]
    if opacity is not None:
        icon["layer0.opacity"] = opacity
    return icon
