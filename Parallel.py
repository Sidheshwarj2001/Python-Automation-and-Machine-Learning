# multi burner

import os
import multiprocessing

def square(No):
    print("PID of worker process is {} for the input {}".format(os.getpid(),No))
    return No*No

def main():
    print("Process ID of our application is : ",os.getpid())
    Data = [1,2,3,4,5]
    Result = []

    pobj = multiprocessing.Pool() #pool like tank kiva taki
    Result = pobj.map(square,Data)

    print("Result after square operation is : ",Result)

if __name__ == '__main__':
    main(
