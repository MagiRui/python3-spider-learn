#!/usr/bin/env/python
#coding:utf8
#author:MagiRui


print(">>>>>>>>>6 显式等待<<<<<<<<")
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, "q")))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-search")))
print(input, button)

print(">>>>>>>>>>>>>19 前进 后退 <<<<<<<<<")
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.baidu.com/")
browser.get("https://www.taobao.com/")
browser.get("https://www.python.org/")
time.sleep(1)
browser.forward()
browser.close()

print(">>>>>>>>>30 Cookies<<<<<<<<<")
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.zhihu.com/explore")
print(browser.get_cookies())
browser.add_cookie({"name":"name", "domain":"www.zhihu.com", "value":"germey"})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())

print(">>>>>>>>>41 选项卡管理>>>>>>>>>>")
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
browser.execute_script("window.open()")
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get("https://www.taobao.com")
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get("https://python.org")

print(">>>>>>>55 异常管理<<<<<<")
from selenium import webdriver
browser.get("htps://www.baidu.com")
#browser.find_element_by_id("hello")


print(">>>>>>>>>>61<<<<<<<<<")
from selenium import webdriver
from selenium.common.exceptions import  TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get("https://www.baidu.com")
except TimeoutException:

    print("Time out")

try:
    browser.find_element_by_id("hello")
except NoSuchElementException:

    print("No Element")
finally:

    browser.close()