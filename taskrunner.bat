REM schtasks /create /sc minute /mo 30 /tn "Run jDrive" /tr \\sampras\Data\Progs\SymlinkFix\jDrive.bat

schtasks /create /sc onstart /tn "Run jDrive Fix" /tr \\sampras\Data\Progs\SymlinkFix\jDrive.bat

schtasks /create /tn "Run jDrive Fixer" /tr \\sampras\Data\Progs\SymlinkFix\jDrive.bat /sc onlogon