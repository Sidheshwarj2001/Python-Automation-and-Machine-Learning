from sys import *
import os


def OpenFile(FileName):
    if(os.path.exists(FileName)):
        print("File is exist")
        fd = open(FileName,'r')

        disply_Data = fd.read()

        print(disply_Data)

        fd.close()

    else:
        print("File is not exist")

def main():

    if(len(argv)<2):
        print("Insuffiecient Argument.....")
        exit()
    if(argv[1]=="-h" or argv[1]=="-H"):
        print("HELP: this script accept file name and display it's contain")
        exit()
    if(argv[1]=='-u'or argv[1]=='-U'):
        print("USAGE : Application and File_Name")
        exit()

    OpenFile(argv[1])




if __name__ == '__main__':
    main()