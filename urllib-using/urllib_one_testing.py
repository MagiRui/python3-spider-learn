#!/usr/bin/env python
#coding:utf8
#author:MagiRui


import urllib.request
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode("utf-8"))



print("######post request######");
import urllib.parse
import urllib.request
data = bytes(urllib.parse.urlencode({"word":"hello"}), encoding="utf8")
response = urllib.request.urlopen("https://httpbin.org/post", data=data)
print(response.read())


print("######get request timeout######");
import urllib.request
response = urllib.request.urlopen("https://httpbin.org/get", timeout=10)
print(response.read())


print("######get request timeout exception######");
import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen("https://httpbin.org/get", timeout=0.1)
except urllib.error.URLError as e:

    if isinstance(e.reason, socket.timeout):

        print("time out")

#响应类型
import urllib.request
response = urllib.request.urlopen("https://httpbin.org/get")
print(type(response))

#响应头,状态码
import urllib.request
response = urllib.request.urlopen("https://www.python.org")
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))


import urllib.request
response = urllib.request.urlopen("https://www.python.org")
print("&&&&&&&&&&&&&&")
print(response.read())
print("???????????????")
print(response.read().decode("utf-8"))

import urllib.request

#request object
request = urllib.request.Request("https://python.org")
response = urllib.request.urlopen(request)
print(response.read().decode("utf8"))

from urllib import request, parse
url = "https://httpbin.org/post"
headers = {

    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Host":"httpbin.org"
}

dict={

    "name":"Germey"
}

data = bytes(parse.urlencode(dict), encoding="utf8")
req = request.Request(url=url, data=data, headers=headers, method="POST")
response = request.urlopen(req)
print(response.read().decode("utf8"))

from urllib import request, parse

url = "https://httpbin.org/post"
dict = {

    "name":"Germey"
}
data = bytes(parse.urlencode(dict), encoding="utf8")
req = request.Request(url = url, data = data, method="POST")
req.add_header(headers)
response = request.urlopen(req)
print(response.read().decode("utf8"))


#代理
import urllib.request
