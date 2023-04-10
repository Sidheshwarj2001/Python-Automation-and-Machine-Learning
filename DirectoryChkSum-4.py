from sys import *
import os
import hashlib

def hashfile(path,blocksize=1024):
    file = open(path,'rb')
    hasher = hashlib.md5()
    buf = file.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = file.read(blocksize)

    file.close()

    return hasher.hexdigest()

def DirectoryGetFileChksum(path):
    flag = os.path.isabs(path)

    if flag ==False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName , SubDir, fileNames in os.walk(path):
            print("Current directory is : "+dirName)
            for files in fileNames:
                path = os.path.join(dirName,files)
                file_hash = hashfile(path)

                print(files)
                print("file chksum is : ",file_hash)
                print(' ')

    else:
        print("Invalid path")
        exit()

def main():
    print("Marvellous Infosystems by Sidheshwar Jawale")
    print("Application Name : "+argv[0])

    if(len(argv)!=2):
        print("ERROR : INSUFFICIENT ARGUMENTS")
        exit()

    if(argv[1]=='-u') or (argv[1] == '-U'):
        print("USAGE : ApplicationName AbsolutePath_of_Directory Extension")
        exit()

    if(argv[1] == "-h" ) or (argv[1] == '-H'):
        print("HELP :The script is used to traverse specific directory and display all files which have given Extension ")
        exit()

    try:
        DirectoryGetFileChksum(argv[1])

    except ValueError as v:
        print("Error : Invalid Datatype of input",v)

    except Exception as E :
        print("Error : invalid input" ,E)

if __name__ == '__main__':
    main()