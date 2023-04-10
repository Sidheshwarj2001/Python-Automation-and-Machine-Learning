from sys import *
import os
import shutil

def copyFileFromDirectory(path ,secondDir ,Extension):

    current_path = os.getcwd()

    os.path.join(current_path,secondDir)

    for files in os.listdir(path):
        shutil.copytree(path,secondDir,)

def main():
    print("Application name is : ",argv[0])

    if(len(argv) != 4):
        print("ERROR : Invalid Argument")
        exit()

    if(argv[1]=='-h' ) or (argv[2] == '-H'):
        print("HELP : This script is require Accept two directory name and one file extension")
        exit()

    if(argv[1]=='-u') or (argv[1] == '-U'):
        print("USAGE : The use of this script is Copy specified extension file from directory into second directory")
        exit()

    try:
        copyFileFromDirectory(argv[1],argv[2],argv[3])

    except Exception as E:
        print("Invalid Error ",E)


if __name__ == '__main__':
    main()