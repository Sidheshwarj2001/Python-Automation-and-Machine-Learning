from sys import *
import psutil

def ProcessMonitor(processName):
    listOfProcess = []
    for proc in psutil.process_iter():

        try:
            pinfo = proc.as_dict(attrs = [ 'pid','name','username'])
            if processName.lower() in pinfo['name']:
                listOfProcess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    return listOfProcess


def main():
    print("Welcome to our Process Monitor Application ")
    print("Application name is : "+argv[0])

    if len(argv)!=2:
        print("ERROR : Invalid Number of Argument")
        print("Use -h for help and -u for the usage")
        exit()

    if argv[1] == '-h' or argv[1]=='-H':
        print("Help : This script is require process name")
        exit()

    if argv[1] == '-u' or argv[1]=='-U':
        print("USEAGE : This script is use to process monitor and write the proceess in the log file")
        exit()

    # try :
    arr = ProcessMonitor(argv[1])

    if len(arr)>0:
        print(arr)
    else:
        print("*****************Give process is not running*******************")

    #
    # except Exception as E:
    #     print("Invalid Error ",E)



if __name__ == "__main__":
    main()