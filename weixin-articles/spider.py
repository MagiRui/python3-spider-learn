from urllib.parse import urlencode

import requests
from pyquery import pyquery as pq

base_url = "http://weixin.sogou.com/weixin?"
keyword = "风景"
proxy = None
headers={
"Cookie": "",
"Host": "weixin.sogou.com",
"Pragma": "no-cache",
"Referer": "https://weixin.sogou.com/",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

# def get_proxy():
#
#     try:
#
#         response = requests.get("")
#         if response.status_code == 200:
#
#             return response.text
#         return None
#     except ConnectionError:
#
#         return None

def get_proxy():

    return ""

def get_html(url):

    try:

        global proxy
        if proxy:

            proxies = {

                "http": "http://" + proxy
            }

            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:

            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:

            return response.text
        elif response.status_code == 302:

            proxy = get_proxy()
            if proxy:

                print("using Proxy")
                return get_html(url)
            else:

                print("Get Proxy Failed")
                return None
    except ConnectionError:

        return get_html(url)

def get_index(keyword, page):

    data = {

        "query":keyword,
        "type":2,
        "page":page
    }

    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    print(html)
def parse_index(html):

    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:

        yield item.attr("href")

def get_detail(url):

    try:

        response = requests.get(url)
        if response.status_code == 200:

            return response.text
        return None

    except ConnectionError:

        return None

def parse_html(html):

    doc = pq(html)
    title = doc(".rich_media_title").text()
    

def main():

    for page  in range(1, 101):

        html = get_index(keyword, page)
        if html:

            articles_urls = parse_index(html)
            for url in articles_urls:

                article_html = get_detail(url)


if __name__ == "__main__":

    main()