import argparse
import json

from icon_theme import create_icon_theme
from icons import create_icons, icons_path
from preferences import create_preferences


def main(argv=None):
    parser = argparse.ArgumentParser(description="Create icons and preferences for A File Icon.")
    parser.add_argument(
        "-i",
        "--icons",
        action="store_true",
        default=False,
        help="convert svg icons to png",
    )
    parser.add_argument(
        "-p",
        "--preferences",
        action="store_true",
        help="create preferences",
    )
    parser.add_argument(
        "-t",
        "--theme",
        action="store_true",
        default=False,
        help="create file icons theme",
    )

    with open(icons_path("icons.json")) as fp:
        icons = json.load(fp)

    options = parser.parse_args(argv)
    if not options.icons and not options.preferences and not options.theme:
        options.icons = True
        options.preferences = True

    if options.icons:
        print("building icons...")
        create_icons(icons)

    if options.preferences:
        print("building preferences...")
        create_preferences(icons)

    if options.theme:
        print("building file icons theme...")
        create_icon_theme(icons)


if __name__ == "__main__":
    main()
