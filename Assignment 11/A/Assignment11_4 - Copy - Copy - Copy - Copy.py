from sys import *
import time
import os
import hashlib

def hasher(path):
    hash_file = open(path ,'rb')
    hash = hashlib.md5()
    read_file = hash_file.read()

    hash_file.close()

    return hash.hexdigest()

dups={}

def DirectoryTravel(path):
    flag = os.path.isabs(path)

    if flag==False:
        path = os.path.abspath(path)

    exists= os.path.isdir(path)

    if exists:

        for dir ,subdir ,filenames in os.walk(path):
            print("main directory name is : ",dir)

            for files in filenames:
                file_path = os.path.join(dir,files)

                chksumFile = hasher(file_path)

                if chksumFile in dups:
                    dups[chksumFile].append(path)
                else:
                    dups[chksumFile] = [path]

        return dups


def main():
    print("Welcome to our Script ")
    print("Automation Script Name is : "+argv[0])

    if len(argv) !=2:
        print("ERROR : Insufficient Argument")
        print("Use -h for help and -u for the usage of the script")
        exit()

    if argv[1]=='-u' or argv[1]=='-U':
        print("USEAGE : This script is use to find the duplicate file and remove it and write the deleted file in the log")
        exit()
    if argv[1]=='-h' or argv[1]=="-H":
        print("HELP : This script require one argument ")
        print("First Argument name is directory path")
        exit()

    try:
        arr = {}
        arr=DirectoryTravel(argv[1])
        print(arr)

    except Exception as E:
        print("Invalid Error ",E)


if __name__ == '__main__':
    main()