from typing import cast

import sublime

from . import themes
from .utils.decorators import debounce
from .utils.logging import log

PACKAGE_NAME, *_ = __spec__.parent.split(".")
PACKAGE_SETTINGS = "A File Icon.sublime-settings"
USER_SETTINGS = "Preferences.sublime-settings"

_cached_packages = []
_cached_settings = {}
_uuid = "9ebcce78-4cac-4089-8bd7-d551c634b052"


def load_json(res_path):
    return cast("dict[str, sublime.Value]", sublime.decode_value(sublime.load_resource(res_path)))


def add_listener():
    log("Initializing settings")
    package_settings = sublime.load_settings(PACKAGE_SETTINGS)
    for key in load_json(f"Packages/{PACKAGE_NAME}/{PACKAGE_SETTINGS}"):
        if key not in ("dev_mode", "dev_trace"):
            _cached_settings[key] = package_settings.get(key)

    user_settings = sublime.load_settings(USER_SETTINGS)
    _cached_packages = user_settings.get("ignored_packages")

    themes.patch(_cached_settings)

    package_settings.add_on_change(_uuid, _on_change_package)
    user_settings.add_on_change(_uuid, _on_change_user)


def clear_listener():
    sublime.load_settings(PACKAGE_SETTINGS).clear_on_change(_uuid)
    sublime.load_settings(USER_SETTINGS).clear_on_change(_uuid)


@debounce(100)
def _on_change_package():
    is_icons_changed = False

    settings = sublime.load_settings(PACKAGE_SETTINGS)

    for key, value in _cached_settings.items():
        new_value = settings.get(key)
        if value != new_value:
            _cached_settings[key] = new_value
            is_icons_changed = True

    if is_icons_changed:
        log("Icons settings changed")
        themes.patch(_cached_settings, overwrite=True)


def _on_change_user():
    global _cached_packages
    settings = sublime.load_settings(USER_SETTINGS)
    packages = settings.get("ignored_packages", [])
    if packages != _cached_packages:
        _cached_packages = packages

        @debounce(2000)
        def update_overlay():
            themes.patch(_cached_settings, on_demand=True)
