import os
import psutil
from sys import *

def ProcInfoLog():
    listProcess = []

    for proc in psutil.process_iter():
        try:
            proc_info = proc.as_dict(attrs = ["pid","name","username"])
            listProcess.append(proc_info)

        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listProcess

def main():
    print("Automation script name is : "+argv[0])
    arr = ProcInfoLog()

    for process in  arr:
        print(process)

if __name__ == '__main__':
    main()