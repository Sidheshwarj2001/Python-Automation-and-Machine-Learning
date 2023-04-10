import urllib.request
import webbrowser
def is_connectd():

    try:
        urllib.request.urlopen("www.google.com",timeout=1)
        print("INTERNET IS CONNECTED")
        return True

    except urllib.request.URLError as err:
        print("internet is not connected")
        print(err)
        return false

def openLink(links):
    for link in links:
        webbrowser.open(link, new=1)

def main():
    arr = ['www.google.com','www.gmail.com','www.stackoverflow.com']
    if is_connectd:
        openLink(arr)
    else:
        print("ERROR IS FOUND......")


if __name__ == "__main__":
    main()