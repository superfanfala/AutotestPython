#-*-coding:utf-8 -*-
from selenium import webdriver
from reselenium import ReSelenium
import time

# dr=ReSelenium()
# dr.open_url('http://yun.shunwang.com/dealLogin.shtml')
# dr.swich_to_frame('ifm')
# dr.input('id','userName',u'运营_01')
# dr.input('id','passwordInp','a12345')
# dr.click('id','loginButton_YHJ')



import re
reg=re.compile(r"(?<=abc)\d+")
match=reg.search('abc123')
print match.group(0)