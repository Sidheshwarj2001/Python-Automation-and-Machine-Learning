import schedule
import time
import datetime

def fun():
    print("Inside fun",datetime.datetime.now())

def main():
    print("Inside task Schedular")
    print("Current time is : ",datetime.datetime.now())

    schedule.every(1).minute.do(fun)
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()