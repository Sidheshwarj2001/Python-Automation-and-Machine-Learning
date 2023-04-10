import requests
from bs4 import BeautifulSoup


url = "https://www.google.com/"

r = requests.get(url)
html_content = r.content  

# parse  
soup = BeautifulSoup(html_content,'html.parser')

# traverl html tree 


def main():
    pass

if __name__ == "__main__":
    main()
