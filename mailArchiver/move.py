import shutil 
import os
import settings
import log

def iveGotToMoveIt(source,destination, array):
    for x in range(len(array)):
        src = (source+array[x])
        dest = (destination+array[x])
        shutil.copytree(src,dest)
        collectionRes = (src + " =>" + dest)
        log.logger(collectionRes)

def iveGotToMoveItFile(source,destination, array):
    for x in range(len(array)):
        src = (source+array[x])
        dest = (destination+array[x])
        shutil.copy2(src,dest)
        collectionRes = (src + " =>" + dest)
        log.logger(collectionRes)




def archives(binary, index, mdf, ldf):

    binSource = settings.binSource
    indexSource = settings.indexSource
    sqlSource = settings.sqlSource

    #Destinations
    binDest = settings.binDest
    indexDest = settings.indexDest
    sqlDest = settings.sqlDest
    
    iveGotToMoveIt(binSource,binDest,binary)
    iveGotToMoveIt(indexSource,indexDest,binary) #binary and indexes are named the same thus don't need seperate variables
    iveGotToMoveItFile(sqlSource,sqlDest,mdf)
    iveGotToMoveItFile(sqlSource,sqlDest,ldf)
    deleteFolder(binSource,binary)
    deleteFolder(indexSource,binary)
    deleteFile(sqlSource, mdf)
    deleteFile(sqlSource, ldf)


def deleteFolder(source, array):
    for x in range(len(array)):
        shutil.rmtree(source+array[x])
        collectionRes = (source+array[x]+" Deleted")
        log.logger(collectionRes)

def deleteFile(source, array):
    for x in range(len(array)):
        os.remove(source+array[x])        
        collectionRes = (source+array[x]+" Deleted")
        log.logger(collectionRes)



    