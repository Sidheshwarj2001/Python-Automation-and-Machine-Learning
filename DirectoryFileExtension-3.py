from sys import *
import os

def DirectoryGetFileExtension(path , extension):
    flag = os.path.isabs(path)

    if(flag == False):
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirname , subdir , filename in os.walk(path):
            print("Current Folder is : ",dirname)

            for file in filename:
                if(file .lower().endswith(extension)):
                    print(file)
                    print(" ")

    else:
        print("Invalid Path")

def main():
    print("Marvellous Infosystems by Sidheshwar Jawale")
    print("Application Name : "+argv[0])

    if(len(argv)!=3):
        print("ERROR : INSUFFICIENT ARGUMENTS")
        exit()

    if(argv[1]=='-u') or (argv[1] == '-U'):
        print("USAGE : ApplicationName AbsolutePath_of_Directory Extension")
        exit()

    if(argv[1] == "-h" ) or (argv[1] == '-H'):
        print("HELP :The script is used to traverse specific directory and display all files which have given Extension ")
        exit()

    try:
        DirectoryGetFileExtension(argv[1],argv[2])

    except ValueError:
        print("Error : Invalid Datatype of input")

    except Exception :
        print("Error : invalid input")

if __name__ == '__main__':
    main()