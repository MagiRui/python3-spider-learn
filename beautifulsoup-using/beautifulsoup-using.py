#!/usr/bin/env/python
#coding:utf8
#author:MagiRui


html = """ <html><head><title>The Dormouse's story</title></head> <body> <p class="title" name="dromouse"><b>The Dormouse's story</b></p> <p class="story">Once upon a time there were three little sisters; and their names were <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>, <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; and they lived at the bottom of a well.</p> <p class="story">...</p> """
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
print(soup.prettify())
print(soup.title.string)

#标签选择器
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#选择元素
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.p)


print(">>>>>>>>><<<<<<<<<<<<<")
#获取标签的名
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
print(soup.title.name)


#获取标签的属性
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
print(">>>>>>>>>64<<<<<<<<<<")
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
print(soup.p.attrs["name"])
print(soup.p["name"])

#获取标签的内容
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p clss="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
print(">>>>>>>>>>>83<<<<<<<<<<")
soup = BeautifulSoup(html, "lxml")
print(soup.p.string)

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
print(">>>>>>>>>>>98<<<<<<<<<<")
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
print(soup.head.title.string)

#子节点,子孙节点
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
#获取标签p的所有子节点
print(">>>>>>>>>>125<<<<<<<<<")
print(soup.p.contents)
print(">>>>>>>>>>127<<<<<<<<<")
cts = soup.p.contents
for cs in cts:
    print(">>>>>>>>>131<<<<<<")
    print(type(cs))
    print(cs)

print(">>>>>>134<<<<<<")
soup = BeautifulSoup(html, "lxml")
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)

print(">>>>>>>>>>>140>>>>>>>>>>>")
#获取所有的子孙节点
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)

#父节点和祖先节点
print(">>>>>>>>>>147<<<<<<<<<<<<<<")
soup = BeautifulSoup(html, "lxml")
print(soup.a.parent)

print(">>>>>>>>>>151<<<<<<<<<<<<<<")
soup = BeautifulSoup(html, "lxml")
print(type(soup.a.parents))
print(list(enumerate(soup.a.parents)))

#兄弟节点
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
print(">>>>>>>>>>159<<<<<<<<<<<<<<")
print(list(enumerate(soup.a.next_siblings)))
print(list(enumerate(soup.a.previous_siblings)))


#标准选择器
#find_all(name, attrs, recursive, text, **kwargs)
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
print(">>>>>>>>>>168<<<<<<<<<<<<<<")
print(soup.find_all("ul"))
print(soup.find_all("ul")[0])


html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
print(">>>>>>>>>>209<<<<<<<<<<")
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
for ul in soup.find_all("ul"):
    for li in ul.find_all("li"):
        print(li.string)


print(">>>>>>>>>>>217<<<<<<<<<<<<")
html = html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
print(">>>>>>>>>>>>236<<<<<<<<<<<<<")
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
print(soup.find_all(attrs={"id":"list-1"}))
print(soup.find_all(attrs={"name":"elements"}))

print(soup.find_all(id="list-1"))
print(soup.find_all(class_="element"))

#根据文本内容帅选
print(">>>>>>>>>>>>245<<<<<<<<<<<<<")
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
print(soup.find_all(text="Foo"))


print(">>>>>>>>>>>>270<<<<<<<<<<<<<")
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
print(soup.find("ul"))
print(type(soup.find("ul")))

#css选择器
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
print(">>>>>>>>>>>312<<<<<<<<<<<")
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
print(soup.select(".panel .panel-heading"))
print(soup.select("ul li"))
print(soup.select("#list-2 .element"))

print(">>>>>>>>>>>320<<<<<<<<<<<")
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

print(">>>>>>>>>>340<<<<<<<<<<<")
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
for ul in soup.select("ul"):

    print(ul["id"])
    print(ul.attrs["id"])


print(">>>>>>>>>>347<<<<<<<<<<<")
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
for li in  soup.select("li"):
    print(li.get_text())