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
        print(index[x-1])
        selectedIndex.append(index[x-1])
 
    #print(selectedIndex == selectedArray)
    if (selectedIndex == selectedArray) == False:
        print("Sorry folders missing from index folder or are incorrectly named \n Please perform this manually")
        raise SystemExit

def sqlRun(selectedArray, numberSelectionsArray):
            selectedSql = []
            ldf =[]
            mdf = []
            for x in os.listdir("example/sqlexpress"):
                if x.endswith(".ldf"):
                    ldf.append(x)
                else:
                    mdf.append(x)
           
            for x in numberSelectionsArray:
           
                selectedSql.append(index[x-1])
        

            print("LDF ",ldf)
            print("mdf ", mdf)
            #print("SQL Array",selectedSql)

