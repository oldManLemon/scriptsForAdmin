REM A quick creation tool for the symbolic link required for AutoTurn

ECHO "Creating Symbolic Link"

if exist "%AppData%\Autodesk\Vehicle Tracking\Settings" (
    echo "I Exist"
    rmdir /S /Q "%AppData%\Autodesk\Vehicle Tracking\Settings"

    mklink /D "%AppData%\Autodesk\Vehicle Tracking\Settings" "\\sampras\Library\ACAD\Vehicle Tracking\Settings"
    ) ELSE (
        echo "no"
        mklink /D "%AppData%\Autodesk\Vehicle Tracking\Settings" "\\sampras\Library\ACAD\Vehicle Tracking\Settings"
    )


REM mklink /D "%AppData%\Autodesk\Vehicle Tracking\Settings" "\\sampras\Library\ACAD\Vehicle Tracking\Settings"
pause