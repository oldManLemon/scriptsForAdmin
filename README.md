# Work Scripts
These are just some scripts I wrote to deal with some recurring issues at work. 

## jDrive.bat
A simple script that updates group policy. We are having an issue where the group policy randomly changes on certian users in very small areas for no given reason. This script allows them to simply fix that issue. 

## symblinks.bat
Symbolic links are an issue in our enviroment as we use them on the projects folder. This force changes the local group policy to match with the mangage policy in our case.

## shortcutCreator.bat
TODO

## taskCreator & taskrunner.bat 

These two are much and much them same. They create a task that is schedualed to run onlogon. Also to deal with this symbolic link stuff.

## mailArchiver 
GFI mailArchiver is a legacy system I inherited. I have little love for it. Long story short this script allows me to quickly select the files that need to go from the live archvie to the cold storage archive, it allows for the quick sorting and movement of the files. I am hoping to update this so that it can detach the databases first before it will attempt to move the mdf files. 
