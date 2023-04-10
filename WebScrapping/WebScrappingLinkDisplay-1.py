import os
import bs4
import requests
from sys import *


def LinkDisplay(url):
    res = requests.get(url)
    print(type(res))

    soup = bs4.BeautifulSoup(res.text,'html.parser')

    link = soup.findAll("a",href=True)

    return link

def main():
    print("_-_-_-_-_-_-_-_-_-_-Web scrapping Application_-_-_-_-_-_-_-_-_-_-")
    print("_-_-_-_-_-_-_-_-_-_-Link Extraction using Web Scrapping_-_-_-_-_-_-_-_-_-_-")

    if (len(argv)==2):
        print("Name of the Application is "+argv[0])
        if(argv[1]=="-h" or argv[1]=="-H"):
            print("This script is used to fetch link from the website")
            exit()
        if (argv[1] == "-u" or argv[1] == "-U"):
            print("Usage:  ApplcationName")
            exit()

    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    arr = LinkDisplay(url)

    print("link are :")

    for ele in arr:
        print(ele['href'])

if __name__ == "__main__":
    main()