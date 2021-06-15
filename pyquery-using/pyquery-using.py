#!/usr/bin/env/python
#coding:utf8
#author:MagiRui

html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

#css选择器
from pyquery import PyQuery as pq
doc = pq(html)
print("<<<<<<20>>>>>>>>")
print(doc("li"))
print(doc(".item-0"))

print("<<<<<<24>>>>>>>>")
from pyquery import  PyQuery as pq
doc = pq(url="http://www.baidu.com")
print(doc("head"))

#传文件
print("<<<<<<24>>>>>>>>")
from pyquery import  PyQuery as pq
#doc = pq(filename="")
#print(doc("li"))


print("<<<<<<36>>>>>>>>")
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
print(doc("#container .list li"))

print("<<<<<<52 查找子元素>>>>>>>>")
from pyquery import PyQuery as pq
doc = pq(html)
items = doc(".list")
print(type(items))
list = items.find("li")
print(type(list))
print(list)

print("<<<<<<61 子元素>>>>>>>>")
list = items.children()
print(type(list))
print(list)

print("<<<<<<66 子元素>>>>>>>>")
lis = items.children(".active")
print(lis)

print("<<<<<<70>>>>>>>>")
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

from pyquery import PyQuery as pq

doc = pq(html)
items = doc(".list")
container = items.parent()
print(type(container))
print(container)

print("<<<<<<91>>>>>>>>")
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
items = doc(".list")
parents = items.parents()
print(type(parents))
print(parents)

print("<<<<<<112>>>>>>>>")
parent = items.parents(".wrap")
print(parent)


print("<<<<<<117 兄弟元素>>>>>>>>")
from pyquery import PyQuery as pq
doc = pq(html)
li = doc(".list .item-0.active")
print(li.siblings())

print("<<<<<<123 兄弟元素>>>>>>>>")
from pyquery import PyQuery as pq
doc = pq(html)
li = doc(".list .item-0.active")
print(li)
print(li.siblings(".active"))
print(li.siblings())

#遍历
print("<<<<<<117 单个元素>>>>>>>>")
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
lis = doc("li").items()
print(type(lis))
for li in lis:
    print(li)


print("<<<<<<154 获取属性>>>>>>>>")
doc = pq(html)
a = doc(".item-0.active a")
print(a)
print(a.attr('href'))
print(a.attr.href)

print("<<<<<<157 获取文本>>>>>>>>")
doc = pq(html)
a = doc(".item-0.active a")
print(a)
print(a.text())

print("<<<<<<<<<<<<167>>>>>>>>>")
doc = pq(html)
a = doc(".item-0.active")
print(a)
print(a.html())

print("<<<<<<<<<<<<173 dom 操作>>>>>>>>>")
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
li = doc(".item-0.active")
print(li)
li.removeClass("active")
print(li)

print("<<<<<<<<<<<<194>>>>>>>>>")
html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''
from pyquery import  PyQuery as  pq
doc = pq(html)
wrap = doc(".wrap")
print(wrap.text())
wrap.find("p").remove()
print(wrap.text())

print("<<<<<<<<<<<<208>>>>>>>>>")
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)