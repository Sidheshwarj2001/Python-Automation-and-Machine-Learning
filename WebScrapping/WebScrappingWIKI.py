import bs4
import requests

res  = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

print(type(res))

# print(res.text)

soup = bs4.BeautifulSoup(res.text,'html.parser')
print(type(soup))

print(soup.prettify())

title = soup.select('title')
print(title)

print("title is ")

arr = soup.select(".mw-headline")

for i in arr:
    print(i.text)
