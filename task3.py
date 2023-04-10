import schedule
import time
import datetime

def Task_Second():
    print("Task based on seconds gets Schedculed at : ",datetime.datetime.now())

def Task_Minute():
    print("Task based on Minutes gets Schedculed at : ",datetime.datetime.now())

def Task_Hour():
    print("Task based on Hour gets schedculed at : ",datetime.datetime.now())

def Task_Day():
    print("Task based on Day gets schedculed at : ",datetime.datetime.now())

def main():
    print("Inside task Schedular")
    print("Current time is : ",datetime.datetime.now())

    #HERE SCHEDULING OF TIME OF TASK IS SCHEDULED

    schedule.every(1).second.do(Task_Second)
    schedule.every(1).minute.do(Task_Minute)
    schedule.every(1).hour.do(Task_Hour)
    schedule.every().saturday.at("18:00").do(Task_Day)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()