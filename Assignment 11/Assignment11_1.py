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


def FileChkSum(path):

    flag = os.path.isabs(path)

    if flag == False :
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists :
        seperator = "_" *80
        log_path = r"C:\Users\91774\Desktop\Marvellous_Infosystem_Code\Assignment\Assignment 11"
        log_path = os.path.join(log_path,"ChkSumLog.log")
        fd = open(log_path,'w')

        for dir , subdir , filename in os.walk(path):
            print("Current Directory is : ",dir)

            for files in filename:
                path = os.path.join(dir,files)

                file_hash = hashfile(path)
                fd.write(files+":-")
                fd.write(file_hash+'\n')
                fd.write( "_" *80)
                fd.write("\n")

                print(files)
                print("file chksum is : ", file_hash)
                print(' ')

    else:
        print("Invalid path")

def main():
    print("Automation script started with : ",argv[0])

    if(len(argv)<2):
        print("ERROR : Insufficient Argument.......")
        print("use -u for usage and -h for help.... ")
        exit()
    if(argv[1]=='-h' or argv[1]=="-H"):
        print("HELP : This script is used to Display ChkSum of all file in given directory")
        exit()
    if(argv[1]=='-u' or argv[1]=='-U'):
        print("USAGE : provide 1 arguments as")
        print("First Argument is Directory name : ")
        exit()

    try:
        FileChkSum(argv[1])

    except Exception as E:
        print("invalid Error",E)

if __name__ == '__main__':
    main()