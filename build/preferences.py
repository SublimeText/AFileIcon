from pathlib import Path
from textwrap import dedent


def create_preferences(icons):
    template = (
        dedent(
            """
            <?xml version="1.0" encoding="UTF-8"?>
            <plist version="1.0">
              <dict>
                <key>scope</key>
                <string>{scope}</string>
                <key>settings</key>
                <dict>
                  <key>icon</key>
                  <string>{name}</string>
                </dict>
              </dict>
            </plist>
            """
        )
        .lstrip()
        .replace("  ", "\t")
    )
    package_root = Path(__file__).parent.parent

    for name, data in icons.items():
        scopes = set()
        for keys in ("aliases", "syntaxes"):
            for syntax in data.get(keys, []):
                for scope in syntax["scope"].split(","):
                    scopes.add(scope.strip())

        if scopes:
            pref = package_root / "preferences" / (name + ".tmPreferences")
            pref.write_text(template.format(name=name, scope=", ".join(sorted(scopes))))
