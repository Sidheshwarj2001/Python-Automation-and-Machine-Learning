import os
from sys import *

def DirectoryWatcher(Dir_Name):
    
    print("Inside Direcctory watcher method")
    print("Name of input Directory is : ",Dir_Name)

    for folderName , SubFolder , fileNames in os.walk(Dir_Name):

        print("Folder Name is : " +folderName)

        for subf in SubFolder:
            print("SubFolder name of "+folderName+ " is "+subf)

        print(" ")

        for fnames in fileNames:
            print("File inside folder" + folderName + " is "+fnames)

        print(" ")

def main():
    print("Directory Watcher application")

    if(len(argv)<2):
        print("Insufficient arguments")
        exit()

    if(argv[1]=='-h'):
        print("This script will travel the directory and display the name of all the enteries")
        exit()

    if(argv[1]=='-u'):
        print("USAGE : Application_name Directory_Name")
        exit()

    DirectoryWatcher(argv[1])

if __name__ == '__main__':
    main()