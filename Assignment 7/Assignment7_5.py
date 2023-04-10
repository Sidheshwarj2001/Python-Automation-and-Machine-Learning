import time
import threading

def printNumber(no):
    for i in range(0,no+1,1):
        print(i)

def ReverseNumber(no):
    for i in range(no+1,0,-1):
        print(i)

def main():
    print("Enter number : ")
    n = int(input())

    thread1 = threading.Thread(target=printNumber ,args=(n,))
    thread2 = threading.Thread(target=ReverseNumber, args=(n,))

    thread3 = threading.Thread(target=printNumber, args=(n,))
    thread4 = threading.Thread(target=ReverseNumber, args=(n,))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

    thread3.start()
    thread3.join()

    thread4.start()
    thread4.join()

if __name__ == '__main__':

    start_time = time.time()
    main()
    end_time = time.time()

    total_time = end_time - start_time
    print("Total time is : ",total_time)