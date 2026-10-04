import sublime

if int(sublime.version()) < 4206:
    print("A File Icon v4.0.0+ requires ST4206+")

else:
    import sys

    __all__ = [
        "AfiCustomizeFileIconThemeCommand",
        "AfiSelectFileIconThemeCommand",
        "plugin_loaded",
        "plugin_unloaded",
    ]

    # Clear module cache to force reloading all modules of this package.
    prefix = __spec__.parent + "."  # don't clear the base package
    for module_name in [
        module_name
        for module_name in sys.modules
        if module_name.startswith(prefix) and module_name != __name__
    ]:
        del sys.modules[module_name]
    del prefix

    from .core import settings
    from .core.icon_theme import (
        AfiCustomizeFileIconThemeCommand,
        AfiSelectFileIconThemeCommand,
        setup_file_icon_theme,
    )

    def plugin_loaded():
        setup_file_icon_theme()
        settings.add_listener()

    def plugin_unloaded():
        settings.clear_listener()
