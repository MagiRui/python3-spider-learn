import json
from urllib.parse import urlencode


import re
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import requests




headers = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

def get_page_index(offset, keyworkd):

    data={
        "offset": offset,
        "format": "json",
        "keyword": keyworkd,
        "autoload": "true",
        "count": "20",
        "cur_tab": 3
    }

    url = "https://www.toutiao.com/search_content/?"+ urlencode(data)

    try:

        response = requests.get(url, headers = headers)
        if response.status_code == 200:

            return response.text
        return None
    except RequestException:

        print("请求索引页出错")
        return None


def parse_page_index(html):

    data = json.loads(html)
    if data and "data" in data.keys():

        for item in data.get("data"):

            yield item.get("article_url")


def get_page_detail(url):

    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:

            return response.text
        return None
    except RequestException:

        print("请求页面出错",  url)
        return None


def parse_page_detail(html, url):

    soup = BeautifulSoup(html, "lxml")
    title = soup.select("title")[0].get_text()
    images_pattern = re.compile('BASE_DATA.galleryInfo =(.*?)</script>', re.S)
    result = re.search(images_pattern, html)
    if result:

        datas = result.group(1)
        print(datas)
        data = json.loads(datas)
        if data and "sub_images"  in data.keys():

            sub_images = data.get("sub_images")
            images = [item.get("url") for item in sub_images]
            return {
                "title":title,
                "images":images,
                "url":url
            }

def main():

    html = get_page_index(0, "街拍")
    for url in parse_page_index(html):

        html = get_page_detail(url)
        if html:
            parse_page_detail(html, url)


if __name__ == "__main__":

    main()
