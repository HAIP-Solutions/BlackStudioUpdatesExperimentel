@echo off
set INSTALLPATH=%1
rd /s /q "%INSTALLPATH%\lib"
rd /s /q "%INSTALLPATH%\res"
rd /s /q "%INSTALLPATH%\share"
exit 0