## Found an Issue?

If you have any problems, please search for [a similar issue] first, before creating [a new one](https://github.com/SublimeText/AFileIcon/issues) (don't forget to **follow the issue template**).

> Also, check the list of [known issues](https://github.com/SublimeText/AFileIcon/labels/known%20issue) before doing so.

Don't forget to provide your environment details: just choose `A File Icon: Environment` in `Command Palette` and copy them.

## Git Commit Guidelines

We have very precise rules over how our git commit messages can be formatted. This leads to more readable messages that are easy to follow when looking through the project history. But also, we use git commit messages to generate **A File Icon** change log. 

We use [**Angular JS commit guidelines**](https://github.com/angular/angular.js/blob/master/CONTRIBUTING.md#-git-commit-guidelines) (except scope notes: we don't need them).

## Development

### Prerequisites

The CairoSVG dependency needs the `cairo` library being present on the system.

**Linux**

```bash
sudo apt-get install libcairo2
```

**Windows**

You can download the latest release of [`cairo.dll`](https://github.com/preshing/cairo-windows/releases) and place it somewhere Python can load it from.

As a last resort, [Graphviz](https://graphviz.org/) includes `cairo.dll` in its distribution.

### Installation

Navigate to _A File Icon_ root directory and call...

**Linux/MacOS**

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -U -r requirements-dev.txt
```

**Windows**

```cmd
py -m venv .venv
.venv\Scripts\activate
py -m pip install -U -r requirements-dev.txt
```

### Building

Navigate to _A File Icon_ root directory, activate python virtual environment and call...

**Linux/MacOS**

```bash
# build everything
python3 build

# build icons only
python3 build --icons

# build preferences only
python3 build --preferences
```

**Windows**

```cmd
: build everything
py build

: build icons only
py build --icons

: build preferences only
py build --preferences
```

## Want to add new icons?

If you want to add a new icon, please follow these steps:

1. Try to find an icon in one of [these resources](https://github.com/SublimeText/AFileIcon#icons). We always try to be pretty similar to [Atom File Icons](https://github.com/DanBrooker/file-icons) package. If you are unable to find anything – add your own.
2. Add an example file that shows this icon to the `tests` folder.
3. Provide the icon in SVG format and put it in the `icons/svg` directory.
4. Add icon settings to the [icons/icons.json](https://github.com/SublimeText/AFileIcon/blob/develop/icons/icons.json) file.
5. Build and check if the icon looks good (Run _A File Icon: Revert to a Freshly Installed State_ after build to apply your icon).
6. It's recommended to add a link to the package which provides the syntax (see [PACKAGES.md](https://github.com/SublimeText/AFileIcon/blob/develop/PACKAGES.md))

> All that you need to add are the SVG icon, its settings and the example file(s).

> All settings should be alphabetically sorted.

> Please do not change any other files - specially in `icons/multi`, `icons/single` and `preferences` folders.

### Icon

Requirements:

- The size should be `16x16` (`viewBox`).
- The color should be black via `fill="#000"` attribute.
- You should build and check if it looks good. If not, make some tweaks to fit the pixel grid.

Example:

[![ActionScript Icon](https://github.com/SublimeText/AFileIcon/blob/develop/icons/svg/file_type_actionscript.svg)](https://github.com/SublimeText/AFileIcon/blob/develop/icons/svg/file_type_actionscript.svg)

```xml
<svg xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" fill="#000" viewBox="0 0 16 16">
  <path d="M11.174,9.341A2.586,2.586,0,1,1,9.345,6.176,2.586,2.586,0,0,1,11.174,9.341Zm1.389-1.713A6.757,6.757,0,0,1,12.6,4.2,2.639,2.639,0,0,0,7.5,2.879,6.749,6.749,0,0,1,5.958,5.7a6.41,6.41,0,0,1-3,1.766,2.641,2.641,0,1,0,1.368,5.1,6.349,6.349,0,0,1,3.309-.016,6.782,6.782,0,0,1,2.985,1.776,2.611,2.611,0,0,0,3.609-.108,2.639,2.639,0,0,0,.09-3.631A6.786,6.786,0,0,1,12.562,7.628Z"/>
</svg>
```

### Settings

Currently Sublime Text requires syntax definitions to apply icons. This means that you need to have the right syntax package to be able to see icons associated with the language. However we can abuse syntax definitions in order to provide different icons to files with the same underlying syntax but different semantics (`Gulpfile.js`, `package.json` & etc.). That's why we provide two types of icons:

- Syntax (apply via syntax scope).
- Aliases (apply via syntax scope and syntax alias abuse).

For example:

```json
"file_type_git": {
  "color": "orange",
  "syntaxes": [
    {
      "name": "GitSyntaxes",
      "scope": "text.git"
    },
    {
      "name": "Git Misc Packages",
      "scope": "source.git"
    }
  ],
  "aliases": [
    {
      "name": "Shell Script (Git)",
      // `extensions` should be provided for aliases only
      "extensions": [
        ".gitignore",
        ".gitkeep"
      ],
      // It's the scope of the syntax which this alias inherits
      // `base` should be provided for aliases only
      "base": "source.shell",
      "scope": "source.shell.git"
    }
  ]
}
```

These settings will create three files after running the build: 

* `aliases\Shell Script (Git).sublime-syntax`
* `preferences\file_type_git.tmPreferences`

Git icons will be applied to files such as `.gitconfig`, `.gitmodules`, etc. when you install `GitSyntaxes` package. However this package doesn't provide syntaxes for `.gitignore` and `.gitkeep`. That's why `A File Icon` creates syntax alias to `Shell Script` to use its highlighting and git icon on these files.
