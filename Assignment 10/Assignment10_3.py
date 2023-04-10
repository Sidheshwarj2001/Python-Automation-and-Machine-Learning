from sys import *
import os
import shutil

def Directory(firstDir):
    current = os.getcwd()

    newFolder = "B"
    secondDir = os.path.join(current, newFolder)

    for file in os.listdir(firstDir):
        shutil .copytree(firstDir,secondDir)


def main():
    print("Automation script staated with : ",argv[0])

    if(len(argv) != 2):
        print("ERROR : Insufficient Argument ")
        print("use -u for usage and -h for help")
        exit()

    if(argv[1]=='-h' or argv[1] == '-H'):
        print("HELP : This script is used to copy the data of first direcotry to the second directory...")
        exit()

    elif(argv[1] == '-U' or argv[1]=='-u'):
        print("USAGE : This script provide two file name : ")
        print("First Directory extension name : ")
        print("First Directory extension name : ")

        exit()
    else:
        Directory(argv[1])


if __name__ == '__main__':
    main()