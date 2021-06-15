import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool

def get_one_page(url):

    try:

        headers ={"User-Agent":
                      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:

            return response.text
        return None
    except RequestException:

        return None

def parse_one_page(html):

    pattrenS = '<dd>.*?board-index.*?>(\d*)</li>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer>(.*?)</i>.*?fraction">(.*?)</i>.*?</li>.*?</dd>'

    #<dd>.*?board-index.*?>(\d*).*?<p*.?class="name".*?<a.*?">(.*?)</a>.*?star">(.*?)</p>' 能匹配排名,电影名称,主演
    pattern = re.compile('<dd>.*?board-index.*?>(\d*).*?<p*.?class="name".*?<a.*?">(.*?)</a>.*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>', re.S)
    items = re.findall(pattern, html)
    for item in items:

        yield {

            "index":item[0],
            "title":item[1],
            "actor":item[2].strip()[3:],
            "time":item[3].strip()[5:],
            "score":item[4]+ item[5]

        }

def write_to_file(content):

    with open("result.txt", "a", encoding="utf8") as f:

        f.write(json.dumps(content, ensure_ascii=False) + "\n")
        f.close()




def main(offset):

    url = "https://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == "__main__":


    # for  i in range(10):
    #
    #     main(i*10)

    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])
