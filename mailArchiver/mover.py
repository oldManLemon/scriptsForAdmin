import os


def intCheck(number):
    try:
        return int(number)
    except ValueError:
        return False


""" First Get list of Files available for moving and print"""
""" We are going to use binary to scan for file names """
jobsList = os.listdir("example/binary")
# print(jobsList)
for jobs in enumerate(jobsList, start=1):
    print(jobs)

""" Then allow selection of available files"""
actionJobs = input("Please select files, seperate with comma: Eg: 2,4 \n")
actionArray = []

for actions in actionJobs:
    # print(actions)
    if intCheck(actions) == int():
        print("")
    else: 
            # print(actions)
            actionArray.append(int(actions))
  
print(actionArray)

""" Select jobs """
for  x in actionArray:
    print(jobsList[x-1])


""" Then detach database if posssible """

""" Then move files acordingly """
