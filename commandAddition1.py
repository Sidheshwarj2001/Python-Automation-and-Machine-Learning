from sys import *

def Addition(a,b):
    ans = a+b
    return ans

def main():
    if(len(argv)!=3):
        print("Invalid number of Argument ")
        exit() # direct band

    Result = Addition(int(argv[1]),int(argv[2]))

    # sum = int(argv[1])+int(argv[2])
    # print("Sum of two number is : ",sum)

    print("Addition is ",Result)

if __name__ == '__main__':
    main()

