import os
import checker

jobsList = os.listdir("example/binary")

for jobs in enumerate(jobsList, start=1): # 0 cannot be accpted as 0 is not an int
    print(jobs)


actionJobs = input("Please select files, seperate with comma: Eg: 2,4 \n")
actionArray = []

for actions in actionJobs:

    if checker.intCheck(actions) != int():
        print(actions)
        actionArray.append(int(actions))
 
            
  
#print(actionArray)
selected = []
""" Select jobs """
for  x in actionArray:
    print(jobsList[x-1])
    selected.append(jobsList[x-1])
#print("outside",selected)

checker.indexRun(selected,actionArray)
checker.sqlRun(selected, actionArray)