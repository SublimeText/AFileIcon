import functools

import sublime

MESSAGE_PREFIX = "A File Icon"
VALUE_PREFIX = " " * (len(MESSAGE_PREFIX) - 2) + ">>> "


def _tags():
    package_settings = sublime.load_settings("A File Icon.sublime-settings")
    if package_settings.get("dev_mode"):
        return package_settings.get("dev_trace", [])
    else:
        return []


def _trace(*args, tag="standard", **kwargs):
    if tag not in _tags():
        return

    text = []

    for arg in args:
        text.append(str(arg))

    print("".join(text), **kwargs)


def log(*args, **kwargs):
    _trace(MESSAGE_PREFIX, ": ", *args, **kwargs)


def dump(*args, **kwargs):
    _trace(VALUE_PREFIX, *args, **kwargs)


def message(*args, **kwargs):
    text = [MESSAGE_PREFIX, ": "]

    for arg in args:
        text.append(str(arg))

    print("".join(text), **kwargs)


def log_tag(tag):
    return functools.partial(log, tag=tag)


def dump_tag(tag):
    return functools.partial(dump, tag=tag)


log.tag = log_tag
dump.tag = dump_tag
