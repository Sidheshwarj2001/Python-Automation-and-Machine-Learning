import time
import threading

def DisplayEven(No):
    for i in range(1,No,1):
        if(i % 2 == 0):
            print("Even number : ",i)

def DisplayOdd(No):
    for i in range(1,No,1):
        if(i % 2 != 0):
            print("Odd number : ",i)

#  multiple threead with single process
def main():
    print("Demonstartion of Parallel programming using multiple processess")
    Number = 2000

    p1 = threading.Thread(target = DisplayEven, args = (Number,))
    p2 = threading.Thread(target = DisplayOdd, args = (Number,)) # list ahe mhnun tithe coma dila ahe

    # target is keyword argument -


    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main")

if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)