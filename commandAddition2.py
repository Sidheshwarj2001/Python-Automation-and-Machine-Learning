
from sys import *

def Addition(a, b):
    ans = a + b
    return ans

def main():
    print("Welcome to : ",argv[0])

    if (len(argv)==2):
        if(argv[1]=='--U'):
            print("Use the Application is :")
            print("Python Name of application First Number Second number")
            exit()

        if(argv[1]=="--H"):
            print("Help : The application is used to perform addition of 2 number")
            exit()

    if (len(argv) != 3):
        print("Invalid number of Argument ")
        exit()  # direct band

    Result = Addition(int(argv[1]), int(argv[2]))

    # sum = int(argv[1])+int(argv[2])
    # print("Sum of two number is : ",sum)

    print("Addition is ", Result)

    print("Thank you for using our the application ")
    print("sidheshwar Jawale")

if __name__ == '__main__':
    main()

