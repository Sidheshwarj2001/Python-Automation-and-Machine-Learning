from sys import *
import os

def DirectoryTraveler(path):
    flag = os.path.isabs(path)

    if flag==False:
        path = os.path.abspath(path)

    exists =os.path.isdir(path)

    if exists:
        for Foldername ,subFolder , Files in os.walk(path):
            print("Current folder is  : ",Foldername)

            for File in Files:
                print("File is : ",File)
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
        print("HELP :The script is used to traverse specific directory and display all the files ")
        exit()

    try:
        DirectoryTraveler(argv[1])

    except ValueError:
        print("Error : Invalid Datatype of input")

    except Exception :
        print("Error : invalid input")

if __name__ == '__main__':
    main()