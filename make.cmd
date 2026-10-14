@echo off
setlocal
chcp 65001 >nul
pushd %~dp0

if /i "%1" == "all" goto ALL
if /i "%1" == "icons" goto ICONS
if /i "%1" == "prefs" goto PREFS
if /i "%1" == "theme" goto THEME
if /i "%1" == "release" goto RELEASE
goto :usage

:ALL
    uv run build
    goto :eof

:ICONS
    uv run build -i
    goto :eof

:PREFS
    uv run build -p
    goto :eof

:THEME
    uv run build -t
    goto :eof

:RELEASE
    if "%2"== "" goto :usage

    for %%d in ("%~dp0.") do set package=%%~nxd

    echo Createing assets for "%package%"...

    :: create downloadable asset for ST4126+
    set branch=master
    set archive=%package%.sublime-package
    set assets="%archive%#%archive%"
    call git push origin %branch%
    call git tag -f %2 %branch%
    call git archive --format zip -o "%archive%" %2

    :: create the release
    call git push --tags --force
    gh release create --target master -t "v%2" "%2" %assets%
    del /f /q *.sublime-package
    git fetch
    goto :eof

:USAGE
    echo USAGE:
    echo.
    echo   make ^[all^|prefs^|release^|theme^]
    echo.
    echo   release ^<semver^> -- create and publish a release (e.g. 1.2.3)
    goto :eof
