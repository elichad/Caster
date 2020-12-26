@echo off
echo Running DNS/DPI from Dragonfly CLI with Natlink.

set currentpath=%~dp0

timeout 120

TITLE Caster: Status Window
C:\Python27\python.exe -m dragonfly load --engine natlink _*.py --no-recobs-messages

pause 1