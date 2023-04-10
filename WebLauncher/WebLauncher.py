from sys import *
import webbrowser
import re
import urllib.request

def is_connected():
    try:
        urllib.request.urlopen(r"https://www.google.com/",timeout=1)
        return True
    except urllib.request.URLError as err:
        print("Internet is not connected")
        print(err)
        return False

def find(string):
    url = re.findall("^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
,string)
    return url

def webLauncher(path):
    with open(path) as fp:
        for line in fp:
            # print(line)
            url = find(line)
            print(url)
            for str in url:
                webbrowser.open(str,new=2)

def main():
    print("Application name is "+argv[0])

    if len(argv) !=2:
        print("Error : Invalid number of Arguments ")
        exit()
    if(argv[1]=='-h' or argv[1]=='-H'):
        print("HELP : This script is used to open URL which are written in one file ")
        exit()

    if (argv[1] == '-u' or argv[1] == '-U'):
        print("USEAGE : Application Name_of_file")
        exit()

    try:
        connected = is_connected()

        if connected:
            webLauncher(argv[1])
        else:
            print("Unable to connect to internet !.")
    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception as e:
        print("Invalid Error ",e)


if __name__ == "__main__":
    main()