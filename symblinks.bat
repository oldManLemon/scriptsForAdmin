@ECHO OFF
ECHO Manually attempting to change Symbolic Link Evals
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

REM Check the boxes in Group Policy locally
fsutil behavior set SymlinkEvaluation L2L:1
fsutil behavior set SymlinkEvaluation L2R:1
fsutil behavior set SymlinkEvaluation R2L:1
fsutil behavior set SymlinkEvaluation R2R:1
echo Please check that all is enabled, 

fsutil behavior query SymlinkEvaluation
echo you may then need to restart
echo If all links are enabled you should be good to go!
pause