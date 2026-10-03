from os.path import basename
from typing import cast

import sublime
import sublime_plugin

from . import settings

CURRENT_KIND = (sublime.KIND_ID_COLOR_GREENISH, "✓", "Current")
AVAILABLE_KIND = (sublime.KIND_ID_COLOR_DARK, "\a", "Available")


def setup_file_icon_theme():
    try:
        prefs = settings.load_json(f"Packages/User/{settings.USER_SETTINGS}")
    except:
        prefs = {}
    if "file_icon_theme" not in prefs:
        sublime.run_command("afi_select_file_icon_theme")


class AfiSelectFileIconThemeCommand(sublime_plugin.ApplicationCommand):
    def run(self, name):
        prefs = sublime.load_settings(settings.USER_SETTINGS)
        prefs.set("file_icon_theme", name)
        sublime.save_settings(settings.USER_SETTINGS)

    def input(self, args):
        if not args or "name" not in args:
            return FileIconThemeInputHandler()
        else:
            return None


class FileIconThemeInputHandler(sublime_plugin.ListInputHandler):
    def __init__(self):
        self.prefs = sublime.load_settings(settings.USER_SETTINGS)

    def name(self):
        return "name"

    def placeholder(self):
        return "Name"

    def cancel(self):
        self.prefs.set("file_icon_theme", self.original)
        sublime.save_settings(settings.USER_SETTINGS)

    def list_items(self):
        self.original = self.prefs.get("file_icon_theme")
        if self.original and isinstance(self.original, list):
            original = basename(cast(str, self.original[0]))
        elif self.original and isinstance(self.original, str):
            original = basename(self.original)
        else:
            original = ""

        ext = len(".sublime-file-icons")
        items = [
            sublime.ListInputItem(
                text=i[:-ext],
                value=i,
                kind=CURRENT_KIND if i == original else AVAILABLE_KIND,
            )
            for i in sorted(set(map(basename, sublime.find_resources("*.sublime-file-icons"))))
        ]

        for i, item in enumerate(items):
            if item.kind == CURRENT_KIND:
                selected = i
                break
        else:
            selected = 0

        return (items, selected)

    def preview(self, text):
        self.last_previewed = text

        def preview_icon_theme():
            if text == self.last_previewed and text != self.prefs.get("file_icon_theme"):
                self.prefs.set("file_icon_theme", text)

        sublime.set_timeout(preview_icon_theme, 250)

        return ""
