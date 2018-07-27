import shutil 
import os
def iveGotToMoveIt(source,destination, array):
    for x in range(len(array)):
        src = (source+array[x])
        dest = (destination+array[x])
        shutil.copytree(src,dest)


def iveGotToMoveItFile(source,destination, array):
    for x in range(len(array)):
        src = (source+array[x])
        dest = (destination+array[x])
        shutil.copy2(src,dest)


# move.archives(selected, mdfSelected, ldfSelected, indexSelected)
def archives(binary, index, mdf, ldf):

    binSource = "example/binary/"
    indexSource = "example/indexes/"
    sqlSource = "C:/Program Files/Microsoft SQL Server/MSSQL14.SQLEXPRESS/MSSQL/DATA/"

    #Destinations
    binDest = "//hawkeye/Cloud/Other/pythonPrac/binary/"
    indexDest = "//hawkeye/Cloud/Other/pythonPrac/indexes/"
    sqlDest = "//hawkeye/Cloud/Other/pythonPrac/sqlexpress/"
    
    iveGotToMoveIt(binSource,binDest,binary)
    iveGotToMoveIt(indexSource,indexDest,binary)
    iveGotToMoveItFile(sqlSource,sqlDest,mdf)
    iveGotToMoveItFile(sqlSource,sqlDest,ldf)
"""   
    for x in range(len(binary)):
        src = (binSource+binary[x])
        #print("to")
        dest = (binDest+binary[x])
        shutil.copytree(src,dest) """
       



    