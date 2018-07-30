# mailArchiver
This is designed to deal with the files that are outputted from GFI Mail Archiver. The files are in a very particular manner which makes manually copying them and moving them around annoying.  Needs to be run as admin

## How to use
- Firstly you'll need python installed. 
- Then naviagte to the folder, you will need to change the hardcoded sources and destinations I have used, then you excute the script with `python mail.py`. 
- You'll be presented with a list taken from the binary folder. 
- Select the numbers you wish to use. The script will then check against the indexes which if incorrect will exit the program. 
- Then you'll be asked to check the chosen mdf and ldf files. I have not yet automated this process. 
- Select `Y` and the script will then execute. 

### TODO
- Turn into exe, potentially need txt or json to read to read the settings window
- Neaten source and destination options
- AutoCompare mdf with binary
- Clean up moved files once done. 