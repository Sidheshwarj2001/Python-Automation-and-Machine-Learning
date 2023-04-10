import time
import multiprocessing

def DisplayEven(no):
    for i in range(1,no+1,1):
        if(i % 2 == 0):
            print("Even number : ",i)

def DisplayOld(no):
    for i in range(1,no+1,1):
        if(i % 2 != 0):
            print("Odd number : ",i)

def main():
    print("Demostration of parallel  programming using multiple processess")
    number = 2000
    p1 = multiprocessing.Process(target = DisplayEven, args = (number , ))
    p2 = multiprocessing.Process(target = DisplayOld, args = (number , ))

    p1.start()
    p2.start() # schedule the process

    p1.join()
    p2.join() #

    print("End of main")

if __name__ == '__main__':
    # execution time of process

    start_time = time.process_time()
    main()
    end_time = time.process_time()

    print("Execution time is : ", end_time - start_time)