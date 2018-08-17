#-*-coding:utf-8 -*-
from selenium import webdriver
from reselenium import ReSelenium

def driver(url):
    dr=ReSelenium('chrome')
    option = dr.ChromeOptions()
    option.add_argument('disable-infobars')
    browser=webdriver.Chrome('disable-infobars')
    browser.get(url)


url='www.baidu.com'
if __name__ == "__main__":
    driver(url)