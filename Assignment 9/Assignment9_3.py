from sys import *
import os

def CreateNewFile(FileName,CurrentFile):

    if(os.path.exists(FileName)):
        print("File is aleready exist.....")
        exit()
    else:
        fileNew = open(FileName,'w+')
        oldFile = open(CurrentFile,'r')

        data = oldFile.read()

        fileNew.write(data)

        fileNew.close()
        oldFile.close()

        fileNew1 = open(FileName, 'r')
        print(fileNew1.read())


def main():

    print("Applicatin name is : ",argv[0])

    if(len(argv)<2):
        print("ERROR : Invalid Arguments ")
        exit()

    if(argv[1] == '-h' or argv[1] == '-H'):
        print("HELP  : This scrip require one file name to copy the containt the file into new file")
        exit()

    if(argv[1] == '-u' or argv[1] == '-U'):
        print("USAGE : Application_name Directory_Name")
        exit()

    CreateNewFile(argv[1],CurrentFile="Demo.txt")

if __name__ == '__main__':
    main()