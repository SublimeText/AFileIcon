# A File Icon

![preview][img-logo]

[![Star on GitHub][img-stars]][stars]
[![Join the chat at Sublime Forum][img-forum]][forum]

This package adds file-specific icons to Sublime Text for improved visual grepping. It's heavily inspired by [Atom File Icons](https://github.com/file-icons/atom).

Its aims are:

* Provide globally available file type specific icons for each UI themes, whether they provide their own file type specific icons or not.

* Display file icons, even if required syntax definition is not installed.

* Display specific icons for files, no dedicated syntax definition exists for.

If you have any problems, please search for a similar issue first, before creating [a new one][new-issue]. 

> Also, check the list of [known issues][known-issues] before doing so.

## Users

### Installation

#### Package Control

The easiest way to install is using Sublime's [Package Control][downloads]. It's listed as `A File Icon`.

1. Open `Command Palette` using menu item `Tools → Command Palette...`
2. Choose `Package Control: Install Package`
3. Find `A File Icon` and hit `Enter`

#### Download

1. [Download the `.zip`][release]
2. Unzip and rename folder to `A File Icon`
3. Copy folder into `Packages` directory, which you can find using the menu item `Preferences → Browse Packages...`

> **Note:** Don't forget to restart Sublime Text after installing this package. 

### Selecting Icon Theme

As of ST4206, file icons are specified by "file icon themes".

To activate A File Icon's theme, add the following line to your user prferences.

```jsonc
{
    "file_icon_theme": "A File Icon.sublime-file-icons",
}
```

For monochrome icons specify

```jsonc
{
    "file_icon_theme": "A File Icon (Mono).sublime-file-icons",
}
```

### Customization

You can change the color, opacity level and size of the icons by modifying your user preferences file, which you can find by:

* `Preferences → Package Settings → A File Icon → Settings`,
* Choose `A File Icon: Settings` in `Command Palette`.

## Developers

### Bring support file icon customization to your theme
 
As of Sublime Text 4206, dedicated icon themes are supported, which A File Icon v4 relies on.

A side effect is it no longer merging its icons into those shipped with themes.

Ideally, icon themes are deployed by dedicated packages to fully separate them from themes or color schemes.

If theme packages ship icons, a related `.sublime-file-icons` file is to be defined for them to be selectable by end users.

The `.supports-a-file-icon-customization` is still evaluated to decide how to create icon related theme patches.

### How It Works

In simple terms, `A File Icon` does the following:

1. Searches all installed themes
3. Checks if themes are already patched, if not
4. patches them by generating `<theme-name>.sublime-theme` files from a [template][template]

The real process is just a little bit more complex to minimize hard drive I/O.

## Resources

### Colors

Colors are bright because they should look good with most themes. However you can change color and opacity level of all icons. See [customization][customization].

![Palette][img-palette]

### Icons

This package contains icons provided by:

- [Atom File Icons](https://github.com/file-icons/atom)
- [Devicons](http://vorillaz.github.io/devicons/#/main)
- [Font Awesome](http://fontawesome.io/)
- [Font Mfizz](http://fizzed.com/oss/font-mfizz)
- [Icomoon](https://icomoon.io/)
- [Octicons](https://octicons.github.com/)

Source icons are provided in SVG format (Sublime Text doesn't currently support it). They are convert to @1x and @2x PNG assets before each release via python build script `uv -m build -i`.

Rasterized icons can be found in `icons` folder.

<!-- Misc -->

[customization]: https://github.com/deathaxe/sublime-a-file-icon#customization
[downloads]: https://packagecontrol.io/packages/A%20File%20Icon 'A File Icon @ Package Control'
[forum]: https://forum.sublimetext.com/t/a-file-icon-sublime-file-specific-icons-for-improved-visual-grepping/25874
[icons]: https://github.com/deathaxe/sublime-a-file-icon/tree/develop/icons/colored
[known-issues]: https://github.com/deathaxe/sublime-a-file-icon/labels/known%20issue
[new-issue]: https://github.com/deathaxe/sublime-a-file-icon/issues/new
[packages]: https://github.com/deathaxe/sublime-a-file-icon/blob/develop/PACKAGES.md
[release]: https://github.com/deathaxe/sublime-a-file-icon/releases
[stars]: https://github.com/deathaxe/sublime-a-file-icon/stargazers
[template]: https://github.com/deathaxe/sublime-a-file-icon/blob/develop/common/templates/theme.py
[issues]: https://github.com/deathaxe/sublime-a-file-icon/issues

<!-- Assets -->

[img-forum]: media/reply-on-forum.svg
[img-getting-started]: media/getting-started.jpg
[img-logo]: media/logo.png
[img-palette]: media/palette.png
[img-stars]: media/star-on-github.svg
