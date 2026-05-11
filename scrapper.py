import requests
from bs4 import BeautifulSoup

keyworld="파이썬"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

lis = soup.find_all("li", class_="c_col")
# print(len(lis))
# print(lis)

for li in lis[:1]:
    company = li.find("a", class_="cpname")
    print(company)
    