#-*-coding:utf-8 -*-
import selenium
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ReSelenium:
    def __init__(self,browser='chrome'):
        dr=''
        if browser == "firefox" or browser == "ff":
            dr = webdriver.Firefox()
        elif browser == "chrome" or browser == "Chrome":
            dr = webdriver.Chrome()
        elif browser == "internet explorer" or browser == "ie":
            dr = webdriver.Ie()
        try:
            self.driver = dr
            #self.my_print("{0} Start a new browser: {1}, Spend {2} seconds".format('success',browser,time.time()-t1))
        except Exception:
            raise NameError("找不到浏览器 {0} ,你可以使用 'ie','ff',"
                            "'chrome'.".format( browser))

    def explicit_wait(self):
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_all_elements_located((By.LINK_TEXT,'text')))

    element=''
    def get_element(self,method='id',path=None):
        if method == 'id':
            element=self.driver.find_element_by_id(path)
        elif method == 'xpath':
            element=self.driver.find_element_by_xpath(path)
        elif method == 'css':
            element=self.driver.find_element_by_css_selector(path)
        elif method == 'class':
            element=self.driver.find_element_by_class_name(path)
        return element

    def open_url(self,url):
        self.driver.get(url)

    def click(self,method,path):
        ele=self.get_element(method,path)
        ele.click()

    def input(self,method,path,text):
        ele=self.get_element(method,path)
        ele.send_keys(text)

    def swich_to_frame(self,path):
        self.driver.switch_to_frame(path)


























