from sys import *
import psutil

def LogFile(arr,log_filename):
    fd = open(log_filename,'w')
    fd.write("_"*60+"\n")

    for process in arr:
        fd.write('%s\n' %process)
        fd.write("_" * 50 + "\n")

    fd.close()

def ProcessMonitor():
    listprocess = []

    for proc in psutil.process_iter():

        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombiesProcess):
            pass

    return listprocess

def main():
    print("Welcome to our Process Monitor Application ")
    print("Application name is : " + argv[0])

    if len(argv) != 2:
        print("ERROR : Invalid Number of Argument")
        print("Use -h for help and -u for the usage")
        exit()

    if argv[1] == '-h' or argv[1] == '-H':
        print("Help : This script is require process name")
        exit()

    if argv[1] == '-u' or argv[1] == '-U':
        print("USEAGE : This script is use to process monitor and write the proceess in the log file")
        exit()

    # try:
    arr = []
    arr = ProcessMonitor()

    LogFile(arr ,argv[1])
#
    # except Exception as E:
    #     print("INVALID ERROR.....")



if __name__ == "__main__":
    main()