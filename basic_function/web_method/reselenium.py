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

    def explicit_wait(self,mathod,path,message):
        if mathod == 'id':
            WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.ID,path)),message)
        elif mathod == 'xpath':
            WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH)),message)
        elif mathod == 'css':
            WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR)),message)
        elif mathod == 'class':
            WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CLASS_NAME)),message)
        elif mathod == 'name':
            WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.NAME)),message)

    def get_element(self,mathod='id',path=None):
        if mathod == 'id':
            self.driver.find_element_by_id(path)
        elif mathod == 'xpath':
            self.driver.find_element_by_xpath(path)
        elif mathod == 'css':
            self.driver.find_element_by_css_selector(path)
        elif mathod == 'class':
            self.driver.find_element_by_class_name(path)
        elif mathod == 'name':
            self.driver.find_element_by_name(path)

    def open_url(self,url,mathod,path):
        self.driver.get(url)
        for i in range(5):
            try:
                self.get_element(mathod,path)
                print('正常打开网页')
                break
            except:
                if i != 4:
                    self.driver.refresh()
                else:
                    print('无法访问到网页！')

    def max_window(self):
        self.driver.maximize_window()

    def set_window_size(self,wide,high):
        self.driver.set_window_size(wide,high)











if __name__ == '__main__':
    ReSelenium().open_url('http://www.baidu.com','id','su')




















