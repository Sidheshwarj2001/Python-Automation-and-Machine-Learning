import os


def main():
    print("PID of current process is  : ", os.getpid())

    print("PID of parent process is : ",os.getppid())

    #command promopt cha p
    #same rahoto ha karan ha command prompt cha ahe mhunun
    #joparent rahoto navin cmd open nahi karan
    # navin process navin pid bheteto

if __name__ == "__main__":
    main()