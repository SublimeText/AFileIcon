import json
from pathlib import Path

PACKAGE_ROOT = Path(__file__).parent.parent


def create_icon_theme(icons):
    ext_icon_mapping = {}

    for name, data in icons.items():
        for key in ("aliases", "syntaxes"):
            for alias in data.get(key, []):
                for ext in alias.get("extensions", []):
                    ext_icon_mapping[ext] = name
                    # add upper-case variant of lower-case extensions
                    if "." not in ext and ext == ext.lower():
                        ext_icon_mapping[ext.upper()] = name

    text = json.dumps(
        {
            "icons": {
                key: value
                for key, value in sorted(ext_icon_mapping.items(), key=lambda i: i[0].lower())
            }
        },
        indent="\t",
    )

    theme = PACKAGE_ROOT / "icons/color/A File Icon.sublime-file-icons"
    theme.write_text(text)
    theme = PACKAGE_ROOT / "icons/mono/A File Icon (Mono).sublime-file-icons"
    theme.write_text(text)
