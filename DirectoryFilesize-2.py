from sys import *
import os
import hashlib

def DirectoryGetFileSize(path):
    flag = os.path.isabs(path)

    if(flag == False):
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName , subdirs , Files in os.walk(path):
            print("Current folder is : ",argv[0])
            for file in Files:
                print("File inside ",dirName," is ",file)
                print("with size : ",os.path.getsize(os.path.join(dirName,)))
                print(' ')

    else:
        print("Invalid Path")
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
        print("HELP :The script is used to traverse specific directory and display all the size of the files ")
        exit()

    try:
        DirectoryGetFileSize(argv[1])

    except ValueError:
        print("Error : Invalid Datatype of input")

    except Exception :
        print("Error : invalid input")

if __name__ == '__main__':
    main()