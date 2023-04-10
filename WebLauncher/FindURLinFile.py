from sys import *
import re

def is_url(string):
    reEx_url ="^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

    url = re.findall(reEx_url,string)

    return url

def FindURL(path):
    fd = open(path,'r')

    for line in fd:
        # print(line)
        valid_url = is_url(line)
        for url in valid_url:
            print(url)

def main():
    try:
        FindURL(argv[1])
    except ValueError:
        print("Invalid Data type ")

    except Exception as E:
        print("Invalid Error "+E)
if __name__ == '__main__':
    main()