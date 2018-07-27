import shutil 
import os
import settings
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



def archives(binary, index, mdf, ldf):

    binSource = settings.binSource
    indexSource = settings.indexSource
    sqlSource = settings.sqlSource

    #Destinations
    binDest = settings.binDest
    indexDest = settings.indexDest
    sqlDest = settings.sqlDest
    
    iveGotToMoveIt(binSource,binDest,binary)
    iveGotToMoveIt(indexSource,indexDest,binary)
    iveGotToMoveItFile(sqlSource,sqlDest,mdf)
    iveGotToMoveItFile(sqlSource,sqlDest,ldf)

       



    