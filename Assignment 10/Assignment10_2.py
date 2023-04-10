from sys import *
import os

def Directory(Dir_Name,File_Extension,Update_Extension):
    fd = open("Data-2.txt",'w')
    for folderName,SubFolderName ,FileName in os.walk(Dir_Name):

        for files in FileName:
            if(files.endswith(File_Extension)):
                fd.write(files.replace(File_Extension,Update_Extension)+"\n")


def main():
    print("Automation script staated with : ",argv[0])

    if(len(argv) != 4):
        print("ERROR : Insufficient Argument ")
        print("use -u for usage and -h for help")
        exit()

    if(argv[1]=='-h' or argv[1] == '-H'):
        print("HELP : This script is used to renamed the file name with another file...")
        exit()

    elif(argv[1] == '-U' or argv[1]=='-u'):
        print("USAGE : This script provide two file name : ")
        print("First Directory extension name : ")
        print("Second file Extension: ")
        print("Third file Extension: ")
        exit()
    else:
        Directory(argv[1],argv[2],argv[3])



if __name__ == '__main__':
    main()