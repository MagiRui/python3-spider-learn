#coding:utf8
#author:MagiRui


import requests
from bs4 import BeautifulSoup


headers = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
response = requests.get("https://www.toutiao.com/a6612180095912116749/", headers=headers)
html = response.text
print(html)
soup = BeautifulSoup(html, "lxml")
print(soup.select("title")[0].get_text())