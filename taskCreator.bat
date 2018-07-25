@ECHO OFF
ECHO Create a task for logon to run gpupdate
ECHO You will need to run this bat with administrative permissions or it will not work. It will close the cmd if no admin permissions found. 
ECHO You can do this by right click this bat file and selecting 'Run as administrator'
call ECHO You should only need to run this once. 

pause
REM Below checks for admin rights (not nesccary but seems to work better)
goto check_Permissions

:check_Permissions
    echo Administrative permissions required. Detecting permissions...

    net session >nul 2>&1
    if %errorLevel% == 0 (
        echo Success: Administrative permissions confirmed.
    ) else (
        echo Failure: Current permissions inadequate.  Please run as administrator
        PING 127.0.0.1 > NUL 2>&1
        EXIT /B 1
    )
net use p: \\sampras\Data\Progs

    schtasks /create /tn "Run jDrive Fixer" /tr p:\SymlinkFix\jDrive.bat /sc onlogon