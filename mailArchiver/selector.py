import os
import checker
import time
import move
import detach


jobsList = os.listdir("example/binary")

for jobs in enumerate(jobsList, start=1):  # 0 cannot be accpted as 0 is not an int
    print(jobs)


actionJobs = input("Please select files, seperate with comma: Eg: 2,4 \n")
actionArray = []

for actions in actionJobs:

    if checker.intCheck(actions) != int():
       # print(actions)
        actionArray.append(int(actions))


# print(actionArray)
selected = []
""" Select jobs """
for x in actionArray:
    # print(jobsList[x-1])
    selected.append(jobsList[x-1])
# print("outside",selected)

indexSelected = checker.indexRun(selected, actionArray)
mdfSelected, ldfSelected = checker.sqlRun(selected, actionArray)
print("Please manaully check to see if the SQL indecies are the correctly selected")
""" TODO Automatically check file names in with SQL indices """

print("BIN", selected)

print("MDF", mdfSelected)

print("LDF", ldfSelected)

confirm = input(
    "\n \nDo you agree these are the files that should be moved? Y/N ")
if confirm.upper() != "Y":
    print("Damnit sorry, the program will now exit")
    time.sleep(3)
    raise SystemExit

# Here use our selector to select our databases and clear them out
for x in range(len(selected)):
    detach.detach(selected[x])

#move.archives(selected, indexSelected, mdfSelected, ldfSelected)
move.archives(selected, indexSelected, mdfSelected, ldfSelected)
