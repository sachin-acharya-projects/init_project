@ECHO OFF

REM Getting the Script Directory
SET "SCRIPT_DIR=%~dp0"

REM Getting Parentfolder, by removing /bin/ from the string
SET "SCRIPT_DIR_N=%SCRIPT_DIR:~0, -5%"

REM Executing Python File
python %SCRIPT_DIR_N%\main.py %1 %2 %3 %4 %5 %6 %7 %8 %9