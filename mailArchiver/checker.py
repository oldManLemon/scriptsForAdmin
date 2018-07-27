import os

def intCheck(number):
    try:
        return int(number)
    except ValueError:
        return False

def indexRun(selectedArray, numberSelectionsArray):

    index = os.listdir("example/indexes")
    selectedIndex =[]
    #print(index)
    for x in numberSelectionsArray:
       # print(index[x-1])
        selectedIndex.append(index[x-1])
 
    #print(selectedIndex == selectedArray)
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
            
            for x in os.listdir("C:\Program Files\Microsoft SQL Server\MSSQL14.SQLEXPRESS\MSSQL\DATA"):
                if x.endswith(".ldf"):
                    ldf.append(x)
                else:
                    mdf.append(x)
           
            for x in numberSelectionsArray:
           
                ldfSelected.append(ldf[x-1])
                mdfSelected.append(mdf[x-1])
        
           
            #print("MDFs ",mdfSelected)
            #print("LDFs ",ldfSelected)
            return mdfSelected, ldfSelected
            #print("SQL Array",selectedSql)

