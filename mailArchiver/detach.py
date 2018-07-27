import pyodbc

server = 'hasea\SQLEXPRESS'
database = 'master'
username = 'nbar'
password = 'nb'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor2 = cnxn.cursor()
cnxn.autocommit=True
sqlNoResultsExpected = "SET NOCOUNT ON;"
sqlDETACH = 'EXEC sp_detach_db "'
sqlDETACHend = '", "true";'


#cursor.execute("SELECT @@version;")
#cursor.execute('ALTER Database "detachMe" Set offline;')
# try:
#     cursor2.execute('SET NOCOUNT ON;')
#     cursor.execute('EXEC sp_detach_db "detachMofo", "true";')
#     #row = cursor()
#   #  row = cursor.fetchone()
#     print ("Great sucess?")
# except TypeError as err:
#     print(err)


print("I keep running??")

def detach(database):
    
    print("Detaching ", database+".dbo")
    try:
        cursor2.execute(sqlNoResultsExpected)
        cursor.execute(sqlDETACH+database+sqlDETACHend)
        #print(sqlDETACH+database+sqlDETACHend)
        #print ("Great sucess?")
    except TypeError as err:
        print(err)
    print(database, "succesfully detached")
