#!/usr/bin/env python
#coding:utf8
#author:MagiRui

import re


"""
元字符
.	匹配除换行符以外的任意字符
\w	匹配字母或数字或下划线或汉字
\s	匹配任意的空白符
\d	匹配数字
\b	匹配单词的开始或结束
^	匹配字符串的开始
$	匹配字符串的结束

重复
*	重复零次或更多次
+	重复一次或更多次
?	重复零次或一次
{n}	重复n次
{n,}	重复n次或更多次
{n,m}	重复n到m次


*?	重复任意次，但尽可能少重复
+?	重复1次或更多次，但尽可能少重复
??	重复0次或1次，但尽可能少重复
{n,m}?	重复n到m次，但尽可能少重复
{n,}?	重复n次以上，但尽可能少重复

\W	匹配任意不是字母，数字，下划线，汉字的字符
\S	匹配任意不是空白符的字符
\D	匹配任意非数字的字符
\B	匹配不是单词开头或结束的位置
[^x]	匹配除了x以外的任意字符
[^aeiou]	匹配除了aeiou这几个字母以外的任意字符
"""


#re.match函数
#re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

content = "Hello 123 4567 World_This is a Regex Demo"

print(len(content))
result = re.match("^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$", content)

#匹配结果对象
print(result)
#匹配的字符串
print(result.group())
#匹配的范
print(result.span())


result = re.match("^Hello.*Demo$", content)
#匹配结果对象
print(result)
#匹配的字符串
print(result.group())
#匹配的范
print(result.span())


print(">>>>>>>>>>>匹配目标")
#匹配目标
content = "Hello 1234567 World_This is a Regex Demo"
result = re.match("^Hello\s(\d+)\sWorld.*Demo$", content)
#匹配结果对象
print(result)
#匹配的字符串
print(result.group(1))
#匹配的范
print(result.span())


print("贪婪匹配")
#贪婪匹配
content = "Hello 1234567 World_This is a Regex Demo"
result = re.match("^He.*(\d+).*Demo", content)
#匹配结果对象
print(result)
#匹配的字符串
print(result.group(1))
#匹配的范
print(result.span())

print("非贪婪匹配")
#贪婪匹配
content = "Hello 1234567 World_This is a Regex Demo"
result = re.match("^He.*?(\d+).*Demo", content)
#匹配结果对象
print(result)
#匹配的字符串
print(result.group(1))
#匹配的范
print(result.span())

print("匹配模式")
content = """Hello 1234567 World_This
is a Regex Demo
"""
#匹配不到任何内容, .不能匹配换行符
result = re.match("^He.*?(\d+).*?Demo$", content)
print(result)


"""
正则表达式修饰符 - 可选标志
正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志：

修饰符	描述
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
"""
result = re.match("^He.*?(\d+).*?Demo$", content, re.S)
print(result)
print(result.group(1))
#匹配的范
print(len(content))
print(result.span())


print("转义")
content = "price is $5.00"
result = re.match("price is \$5\.00", content)
print(result)


#re.match与re.search的区别
#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。

print("re.search")
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.search("Hello.*?(\d+).*?Demo", content)
print(result)
print(result.group(1))



html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''


result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
print(result)
print(result.group(1), result.group(2))

result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
print(result)
print(result.group(1), result.group(2))

result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
print(result)
print(result.group(1), result.group(2))

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''
result = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(result)
for  rlt in result:

    print(rlt[0], rlt[1], rlt[2])


result = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
for rlt in result:

    print(rlt)

#字符串替换
#re.sub


print("just do it")
#实战联系
import re
import requests
content = requests.get("https://book.douban.com/").text


#pattern = re.compile("<li.*?cover.*?href=\"(.*?)\".*?title=\"(.*?)\".*?more-meta.*?author\">(.*?)</span>.*?year>(.*?)</span>.*?</li>", re.S)
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
results = re.findall(pattern, content)
for book in results:
    url, name, author, date = result
    author = re.sub('\s', '', author)
    date = re.sub('\s', '', date)
    print(url, name, author, date)

