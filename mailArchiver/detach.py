import pyodbc
import settings
import log
server = settings.server
database = settings.database
username = settings.username
password = settings.password

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor2 = cnxn.cursor()
cnxn.autocommit=True
sqlNoResultsExpected = "SET NOCOUNT ON;"
sqlOffline = 'AlTER DATABASE "' + database+ '" SET OFFLINE'
sqlDETACH = 'EXEC sp_detach_db "'
sqlDETACHend = '", "true";'

def detach(database):
    
    print("Detaching ", database+".dbo")
    try:
        cursor2.execute(sqlNoResultsExpected)
        cursor.execute(sqlDETACH+database+sqlDETACHend)
        #print(sqlDETACH+database+sqlDETACHend)
        #print ("Great sucess?")
        collectionLog= (database, "successfully detached")
        log.logger(collectionLog)
        print(database, "succesfully detached")
    except pyodbc.ProgrammingError as err:
        print(err)
        print("The Database is already detached")
        collErr = (database,"Already appears to be detached see err \n", err)
        log.logger(collErr)


    
