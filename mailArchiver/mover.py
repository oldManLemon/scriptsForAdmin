import os

""" First Get list of Files available for moving and print"""
""" We are going to use binary to scan for file names """
jobsList = os.listdir("example/binary")
# print(jobsList)
for jobs in enumerate(jobsList):
    print(jobs)

""" Then allow selection of available files"""
 actionJobs = raw_input("Please select files, seperate with comma: Eg: 2,4 \n")

for actions in range(int(actionJobs)):
    print(actions)

""" Then detach database if posssible """

""" Then move files acordingly """

