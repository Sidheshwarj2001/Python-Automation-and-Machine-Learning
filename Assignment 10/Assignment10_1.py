from sys import *
import os

def DirectoryWatcher(Dir_Name,Extension):
    fd = open("data-1.txt",'w')
    fd.write("Inside Direcctory watcher method\n")
    fd.write("Name of input Directory is : " + Dir_Name + "\n")

    for folderName, SubFolder, fileNames in os.walk(Dir_Name):
        for file in fileNames:
            if(file.endswith(Extension)):
                fd.write(file+"\n")

    fd.close()

def main():
    print("Automation script started with : ",argv[0])

    if(len(argv)<2):
        print("ERROR : Insufficient Argument.......")
        print("use -u for usage and -h for help.... ")
        exit()
    if(argv[1]=='-h' or argv[1]=="-H"):
        print("HELP : This script is used to Display all file withe given Extension...")
        exit()
    elif(argv[1]=='-u' or argv[1]=='-U'):
        print("USAGE : provide 2 arguments as")
        print("First Argument is Directory name : ")
        print("Second Argument is Extension : ")
        exit()

    else:
        DirectoryWatcher(argv[1],argv[2])

if __name__ == '__main__':
    main()