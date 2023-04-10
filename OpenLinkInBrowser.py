import webbrowser
import urllib.request

def is_connected():

    try:
        urllib.request.urlopen("www.google.com",timeout=1)
        print("INTERNET IS CONNECTED>>>>>>>>")
        return True
    except urllib.request.URLError as err:
        print("Internet is not connected")
        print(err)
        return False

def openLink(url):
    webbrowser.open(url, new=1, autoraise=True)


def main():
    url = "https://www.google.com"

    if is_connected:
        openLink(url)
    else:
        print("INTERNET IS NOT CONNECTED TO YOUR MACHINE>>><<<>>")

if __name__ == "__main__":
    main()