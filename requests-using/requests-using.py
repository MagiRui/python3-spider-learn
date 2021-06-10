#!/usr/bin/env python
#coding:utf8
#author:MagiRui

import requests

response = requests.get("https://www.baidu.com/")
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)


requests.post("https://httpbin.org/post")
requests.put("https://httpbin.org/put")
requests.delete("https://httpbin.org/delete")
requests.head("https://httpbin.org/get")
requests.options("https://httpbin.org/get")



response = requests.get("http://httpbin.org/get")
print(response.text)


response = requests.get("https://httpbin.org/get?name=MagiRui&age=30")
print(response.text)

data = {

    "name":"MagiRui",
    "age":30
}

response = requests.get("https://httpbin.org/get", params= data)
print(response.text)




import json
response = requests.get("https://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))


response = requests.get("https://github.com/favicon.ico")
print(type(response.text), type(response.content))
#print(response.text)
#print(response.content)
with open("/Users/magirui/python3-spyder/requests-using/favicon.ico", "wb") as f :

    f.write(response.content)
    f.close()


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}


response = requests.get("https://www.zhihu.com/explore", headers=headers)
print(response.text)

data = {"name":"MagiRui", "age":20}
response = requests.post("https://httpbin.org/post", data = data, headers = headers)
print(response.json())




response = requests.get("http://www.jianshu.com")
print(type(response.status_code), response.status_code)
print(type(response.headers), response.headers)
print(type(response.cookies), response.cookies)
print(type(response.url), response.url)
print(type(response.history), response.history)


#文件上传
files = {"file": open("favicon.ico", "rb")}
response = requests.post("https://httpbin.org/post", files = files)
print(response.text)

response = requests.get("https://www.baidu.com")
print(response.cookies)
for key, value in response.cookies.items():

    print(key + "=" + value)

#此时获取到的cookies是空的
requests.get("https://httpbin.org/cookies/set/number/123456789")
response = requests.get("https://httpbin.org/cookies")
print(response.text)

s = requests.Session()
s.get("https://httpbin.org/cookies/set/number/123456789")
response = s.get("https://httpbin.org/cookies")
print(response.text)


#证书验证(此时会有告警),如下打印结果:
#InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
#InsecureRequestWarning)
#200
#通过以下方式消除告警
#from requests.packages import urllib3
#urllib3.disable_warnings()
response = requests.get("https://www.12306.cn", verify= False)
print(response.status_code)

#代理设置
#socks5代理
proxies = {

    "http":"http://127.0.0.1:9743",
    "https":"https://127.0.0.1:9743"
}

"""
proxies = {
    "http":"http://user:password@127.0.0.1:9743"
}
"""
response = requests.get("https://www.taobao.com", proxies=proxies)
print(response.status_code)

#认证
from requests.auth import HTTPBasicAuth
r = requests.get("http://120.27.34.24:9001", auth=HTTPBasicAuth("user", "123"))


