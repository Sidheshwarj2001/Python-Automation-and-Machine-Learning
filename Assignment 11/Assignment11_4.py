from sys import *
import time
import os
import hashlib

def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

dups={}

def DirectoryTravel(path):
    flag = os.path.isabs(path)

    if flag ==False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName , SubDir, fileNames in os.walk(path):
            print("Current directory is : "+dirName)
            for files in fileNames:
                path = os.path.join(dirName,files)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups

    else:
        print("Invalid path")
        exit()

def RemoveDuplicate(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    log_path = r"C:\Users\91774\Desktop\Marvellous_Infosystem_Code\Assignment\Assignment 11"
    file_path = os.path.join(log_path, "DeleteFileLog.txt")

    fd = open(file_path, 'w')
    fd.write("-" * 80 + "\n")
    fd.write(" ")

    icnt = 0
    if len(results) > 0:
        print("Duplicates found : ")
        print("The following files are identetical")

        print("Are you Sure to delete the duplicate file select Y/N")

        res = input()

        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    fd.write(subresult + "\n")
                    fd.write("-" * 80 + "\n")

                    if res == "y" or res == 'Y':
                        os.remove(subresult)
                        print("File Deleted Succssuflly...")
                    else:
                        print("File was not deleted")
            icnt = 0
    else:
        print("No Duplicates are found ")

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
        start_time = time.time()
        arr = {}
        arr=DirectoryTravel(argv[1])
        RemoveDuplicate(arr)
        end_time = time.time()
        print("time required for this script is : ",end_time-start_time)

    except Exception as E:
        print("Invalid Error ",E)

if __name__ == '__main__':
    main()