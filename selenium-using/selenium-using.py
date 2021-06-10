#!/usr/bin/env/python
#coding:utf8
#author:MagiRui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:

    browser.get("https://www.baidu.com")
    input = browser.find_element_by_id("kw")
    input.send_keys("Python")
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "content_left")))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()


from selenium import webdriver
#browser = webdriver.Chrome()
#browser = webdriver.Safari()



print(">>>>>>>>33<<<<<<<<<")
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
print(browser.page_source)
browser.close()

#查找单个元素
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
input_first = browser.find_element_by_id("q")
input_second = browser.find_element_by_css_selector("#q")
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
browser.close()


print(">>>>>>>>>>>>51<<<<<<<<<<<<<")
from selenium import webdriver
from selenium.webdriver.common.by import  By

browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
input_first = browser.find_element(By.ID, "q")
print(input_first)
browser.close()

print(">>>>>>>>>>>>61 多个元素<<<<<<<<<<<<")
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
lis = browser.find_element_by_css_selector(".service-bd li")
print(lis)
print(type(lis))
browser.close()

print(">>>>>>>>>>70<<<<<<<<<<<")
from selenium import webdriver
from selenium.webdriver.common.by import  By

browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
lis = browser.find_element(By.CSS_SELECTOR, ".service-bd li")
print(lis)
browser.close()


from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
print(lis)
browser.close()
print(">>>>>>>>>>>>>>>>80<<<<<<<<<<<<<<<")
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
input = browser.find_element_by_id("q")
input.send_keys("Iphone")
time.sleep(1)
input.clear()
input.send_keys("iPad")
button = browser.find_element_by_class_name("btn-search")
button.click()


print(">>>>>>>>>>>103交互动作<<<<<<<<<<<<")
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser.get(url)
browser.switch_to.frame("iframeResult")
source = browser.find_element_by_css_selector("#draggable")
target = browser.find_element_by_css_selector("#droppable")
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()

print(">>>>>>>>>>>117 js<<<<<<<<<<<<<")
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.zhihu.com/explore")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
browser.execute_script("alert('To Bottom')")


