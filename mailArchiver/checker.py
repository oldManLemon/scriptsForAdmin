import os
import settings
import log

def intCheck(number):
    try:
        return int(number)
    except ValueError:
        return False

def indexRun(selectedArray, numberSelectionsArray):

    index = os.listdir("example/indexes")
    selectedIndex =[]

    for x in numberSelectionsArray:
        selectedIndex.append(index[x-1])
    
    if (selectedIndex == selectedArray) == False:
        print("Sorry folders missing from index folder or are incorrectly named \n Please perform this manually")
        raise SystemExit
    else:
        return selectedIndex

def sqlRun(selectedArray, numberSelectionsArray):
            
            ldf =[]
            ldfSelected= []
            mdf = []
            mdfSelected = []
            
            for x in os.listdir(settings.sqlSource):
                if x.endswith(".ldf"):
                    ldf.append(x)
                else:
                    mdf.append(x)
           
            for x in numberSelectionsArray:
           
                ldfSelected.append(ldf[x-1])
                mdfSelected.append(mdf[x-1])

            log.logger("###Databases being targeted for detachment and removal###")
            log.logger(mdfSelected)
            log.logger(ldfSelected)

            return mdfSelected, ldfSelected

