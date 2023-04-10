from sys import *
import os

def CreateNewFile(FileName1,FileName2):

    if(os.path.exists(FileName1) and os.path.exists(FileName2)):
        print("File is aleready exist.....")

        file1 = open(FileName1,'r')
        file2 = open(FileName2,'r')

        file_read1 = file1.readlines()
        file_read2 = file2.readlines()

        if(file_read1==file_read2):
            print("Successfully........")

        else:
            print("Failure..........")

    else:
        print("ERROR  : file is not exist....")
        exit()

def main():

    print("Applicatin name is : ",argv[0])

    if(len(argv)<2):
        print("ERROR : Invalid Arguments ")
        exit()

    if(argv[1] == '-h' or argv[1] == '-H'):
        print("HELP  : This scrip require two file name to compare the containt the file into new file")
        exit()

    if(argv[1] == '-u' or argv[1] == '-U'):
        print("USAGE : Application_name Directory_Name")
        exit()

    CreateNewFile(argv[1],argv[2])

if __name__ == '__main__':
    main()