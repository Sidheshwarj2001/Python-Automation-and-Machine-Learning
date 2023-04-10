from sys import *
from os import *

def Script_Task(No):
    if(No % 2 == 0):
        print("It is Even number ")
    else:
        print("It is Old Number")

def main():
    print("_________________Marvellous Infosystems Automations")

    print("Automation Script started with name : ",argv[0])

    if(len(argv) != 2):
        print("Error : Insufficient arguments ")
        print("Use -h for help and -u for usage of script")
        exit()

    if(argv[1]=="-h" or argv[1]=="-H"):
        print("Help : This script is used to perform ____________")
        exit()

    elif(argv[1]=="-u" or argv[1]=='-U'):
        print("USAGE : Provide ______ numbers of argument as")
        print("First Argument is :_____")
        print("Second Argument as :_____")
        exit()

    else:
        # print("There is no such option in the script",argv[1])
        # exit()
        Script_Task(int(argv[1]))

if __name__ == '__main__':
    main()