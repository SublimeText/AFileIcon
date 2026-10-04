# A File Icon

![preview][img-logo]

[![Star on GitHub][img-stars]][stars]
[![Join the chat at Sublime Forum][img-forum]][forum]

This Sublime Text package ...

1. provides basic infrastructure to select and customize file icon themes.
2. ships colored and monochrome file icons, heavily inspired by [Atom File Icons](https://github.com/file-icons/atom).

## Installation

### Package Control

The easiest way to install is using Sublime's [Package Control][downloads]. It's listed as `A File Icon`.

1. Open Command Palette using <kbd>ctrl+shift+P</kbd> or menu item `Tools → Command Palette...`
2. Run `Package Control: Install Package`
3. Find `A File Icon` and hit <kbd>Enter</kbd>

### Manual Install

1. Download [AFileIcon.sublime-package](https://github.com/SublimeText/AFileIcon/releases)
2. Rename it to _A File Icon.sublime-package_
3. Copy it into _Installed Packages_ directory

> [!NOTE]
>
> To find _Installed Packages_...
>
> 1. call _Menu > Preferences > Browse Packages.._
> 2. Navigate to parent folder

## Usage

### Select Icon Theme

1. Open Command Palette using <kbd>ctrl+shift+P</kbd> or menu item `Tools → Command Palette...`
2. Run `UI: Select Icon Theme`
3. Choose a theme and hit <kbd>Enter</kbd>

### Customize Icon Theme

1. Open Command Palette using <kbd>ctrl+shift+P</kbd> or menu item `Tools → Command Palette...`
2. Run `UI: Customize Icon Theme`
3. Choose a theme and hit <kbd>Enter</kbd>

An icon theme maps file extension to image names in the following format:

```json
{
    "icons": {
        "extension": "icon_file_name",
    }
}
```

### Customize Icon Settings

To change color, opacity level and size of icons,
modify A File Icon settings:

1. Open Command Palette using <kbd>ctrl+shift+P</kbd> or menu item `Tools → Command Palette...`
2. Run `Preferences: A File Icon Settings`

> [!NOTE]
>
> Settings are applied globally to all icon themes.

## Theme Developers

As of Sublime Text 4206 dedicated icon themes are supported, 
which A File Icon 4.0 relies on.

A side effect is it no longer merging its icons into those shipped with themes.

Ideally, icon themes are deployed by dedicated packages
to fully separate them from themes or color schemes.

If theme packages ship icons,
a related `.sublime-file-icons` file is to be defined
for them to be selectable by end users.

The `.supports-a-file-icon-customization` is still evaluated
to decide how to create icon related theme patches
as former versions of A File Icons did.

## Resources

### Colors

Colors are bright because they should look good with most themes.
However you can change color and opacity level of all icons.
See [customization][customization].

![Palette][img-palette]

### Icons

This package contains icons provided by:

- [Atom File Icons](https://github.com/file-icons/atom)
- [Devicons](http://vorillaz.github.io/devicons/#/main)
- [Font Awesome](http://fontawesome.io/)
- [Font Mfizz](http://fizzed.com/oss/font-mfizz)
- [Icomoon](https://icomoon.io/)
- [Octicons](https://octicons.github.com/)

Source icons are provided in SVG format (Sublime Text doesn't currently support it).
They are convert to @1x and @2x PNG assets before each release
via python build script `uv run build --icons`.

Rasterized icons can be found in `icons` folder.

<!-- Misc -->

[customization]: https://github.com/deathaxe/sublime-a-file-icon#customization
[downloads]: https://packagecontrol.io/packages/A%20File%20Icon 'A File Icon @ Package Control'
[forum]: https://forum.sublimetext.com/t/a-file-icon-sublime-file-specific-icons-for-improved-visual-grepping/25874
[icons]: https://github.com/deathaxe/sublime-a-file-icon/tree/master/icons/color
[known-issues]: https://github.com/deathaxe/sublime-a-file-icon/labels/known%20issue
[new-issue]: https://github.com/deathaxe/sublime-a-file-icon/issues/new
[packages]: https://github.com/deathaxe/sublime-a-file-icon/blob/master/PACKAGES.md
[release]: https://github.com/deathaxe/sublime-a-file-icon/releases
[stars]: https://github.com/deathaxe/sublime-a-file-icon/stargazers
[issues]: https://github.com/deathaxe/sublime-a-file-icon/issues

<!-- Assets -->

[img-forum]: media/reply-on-forum.svg
[img-getting-started]: media/getting-started.jpg
[img-logo]: media/logo.png
[img-palette]: media/palette.png
[img-stars]: media/star-on-github.svg
