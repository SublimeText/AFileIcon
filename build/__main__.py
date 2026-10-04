import argparse

from icon_theme import create_icon_theme

from icons import create_icons, load_icons_json


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
        "-t",
        "--theme",
        action="store_true",
        default=False,
        help="create file icons theme",
    )

    icons = load_icons_json()

    options = parser.parse_args(argv)
    if not options.icons and not options.theme:
        options.icons = True
        options.theme = True

    if options.icons:
        print("building icons...")
        create_icons(icons)

    if options.theme:
        print("building file icons theme...")
        create_icon_theme(icons)


if __name__ == "__main__":
    main()
