import schedule
import time
import datetime
import sys

def fun():
    print("Inside fun",datetime.datetime.now())

def scriptTerminator():
    print("Schedule is exist")
    sys.exit()

def main():
    print("Inside task Schedular")
    print("Current time is : ",datetime.datetime.now())

    schedule.every(1).second.do(fun)
    schedule.every(6).seconds.do(scriptTerminator)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()