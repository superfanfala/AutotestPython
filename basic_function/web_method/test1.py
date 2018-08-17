#-*-coding:utf-8 -*-
from selenium import webdriver
import time

dr=webdriver.Chrome()
dr.get('http://yun.shunwang.com/dealLogin.shtml')
time.sleep(1)
dr.switch_to_frame('ifm')
time.sleep(1)
dr.find_element_by_id('userName').send_keys(u'中文')