from sys import *
import os
import hashlib

def hasher(path,blocksize = 1024):
    hash= hashlib.md5()

    fd = open(path , 'rb')

    buf = fd.read(blocksize)

    while len(buf)>0:
        hash.update(buf)
        buf = fd.read(blocksize)

    fd.close

    return hash.hexdigest()

duplicateDict = dict()

def DirectoryWalker(path):
    flag = os.path.isabs(path)
    if flag==False:
        path = os.path.abspath(path)

    exist = os.path.isdir(path)

    if exist :

        for dir , subdir , filename in os.walk(path):
            print("Main folder name is :" + dir)

            for files in filename:
                path = os.path.join(dir, files)
                file_hash = hasher(path)

                if file_hash in duplicateDict:
                    duplicateDict[file_hash].append(path)
                else:
                    duplicateDict[file_hash] = [path]

        return duplicateDict

    else:
        print("invalid Error")
        exit()

def printDuplicates(dict1):
    results = list(filter(lambda x : len(x)>1, dict1.values()))

    #creating log file at run time
    log_path = r"C:\Users\91774\Desktop\Marvellous_Infosystem_Code\Assignment\Assignment 11"
    log_path_file= os.path.join(log_path,"Assignment11.2logFile.log")

    fd = open(log_path_file , 'w')

    if len(results)>0:
        icnt = 0
        for result in results:
            for subres in result:
                icnt +=1
                if icnt >=2:
                    fd.write(subres +"\n")
                    fd.write("_"*50+"\n")

    else:
        print("No Duplicates are found ")

def main():
    print("Welcome to our Automation script ")

    print("Automation script name is  : ",argv[0])

    if(len(argv) !=2):
        print("Error : Insufficient Argument....")
        print("use -u for usage and -h for help....")
        exit()

    if(argv[1]=='-H' or argv[1]=="-H"):
        print("HELP : This script is used to find duplicate file and write the file name in log")
        exit()

    if(argv[1]=='-u' or argv[1]=="-U"):
        print("USAGE : This script acccept two Argument")
        print("First Argument is directory Name")
        print("Second Argument is log file name")
        exit()

    try:
        arr = {}
        arr = DirectoryWalker(argv[1])
        printDuplicates(arr)

    except Exception as E:
        print("Invalid Error",E)

if __name__ == '__main__':
    main()