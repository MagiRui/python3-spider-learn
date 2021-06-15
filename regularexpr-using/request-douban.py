#!/usr/bin/env python
#coding:utf8
#author:MagiRui

import requests
import re


content = requests.get('https://book.douban.com/').text
print(content)
pattern = re.compile('.*?cover.*?href="(.*?)".*?title="(.*?)', re.S)
results = re.findall(pattern, content)
print(results)
for result in results:
    url, name, author, date = result
    author = re.sub('\s', '', author)
    date = re.sub('\s', '', date)
    print(url, name, author, date)