@echo off
setlocal enabledelayedexpansion
set "newPath=%CD%;%PATH%"
setx PATH "!newPath!" /M