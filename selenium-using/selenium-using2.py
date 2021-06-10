#!/usr/bin/env/python
#coding:utf8
#author:MagiRui

from selenium import webdriver
from selenium.webdriver import ActionChains


print(">>>>>>>>获取属性9<<<<<<<<")
browser = webdriver.Chrome()
url = "https://www.zhihu.com/explore"
browser.get(url)
logo = browser.find_element_by_id("zh-top-link-logo")
print(logo)
print(logo.get_attribute("class"))


print(">>>>>>>获取文本值18<<<<<<<")
from selenium import webdriver
url = "https://www.zhihu.com/explore"
browser.get(url)
input = browser.find_element_by_id("zu-top-add-question")
print(input.text)

print("获取ID、位置、标签名、大小")
from selenium import webdriver
browser = webdriver.Chrome()
url = "https://www.zhihu.com/explore"
browser.get(url)
input = browser.find_element_by_class_name("zu-top-add-question")
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)

print(">>>>>>>>>36<<<<<<<<<<")
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser.get(url)
browser.switch_to.frame("iframeResult")
source = browser.find_element_by_css_selector("#draggable")
print(source)
try:
    logo = browser.find_element_by_class_name("logo")
except NoSuchElementException:

    print("NO Logo")

browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name("logo")
print(logo)
print(logo.text)


printMsg = """
等待
隐式等待
当使用了隐式等待执行测试的时候，如果 WebDriver没有在 DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常, 换句话说，当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间再查找 DOM，默认的时间是0
"""

print(">>>>>>>65<<<<<<<<")
print(printMsg)

from selenium import webdriver
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://www.zhihu.com/explore")
input = browser.find_element_by_class_name("zu-top-add-question")
print(input)