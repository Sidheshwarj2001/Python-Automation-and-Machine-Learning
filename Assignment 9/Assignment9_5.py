from sys import *
import os

def CreateNewFile(FileName1,word):

    if(os.path.exists(FileName1)):
        print("File is aleready exist.....")

        file = open(FileName1,'r')
        data = file.read()

        counter = data.count(word)

        print("Frequency of world is :",counter)

    else:
        print("ERROR  : file is not exist....")
        exit()

def main():

    print("Applicatin name is : ",argv[0])

    if(len(argv)<2):
        print("ERROR : Invalid Arguments ")
        exit()

    if(argv[1] == '-h' or argv[1] == '-H'):
        print("HELP  : This scrip require one file name and one string")
        exit()

    if(argv[1] == '-u' or argv[1] == '-U'):
        print("USAGE : Application_name Directory_Name")
        exit()

    CreateNewFile(argv[1],argv[2])

if __name__ == '__main__':
    main()