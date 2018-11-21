# -*- coding:utf-8 -*-
# 初始化driver，基类, 所有的case类都要继承这个基类
from selenium import webdriver
from NSDAEvent.settings.data import Data
from selenium.webdriver.support.wait import WebDriverWait
from NSDAEvent.locators.login_locator import LoginLocator

class InitDriver(object):

    def get_driver(self):
        self.event_title = Data.event_title
        self.wait_time = Data.wait_time
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(Data.url)
        WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element(LoginLocator.LOGIN_BUTTON[0], LoginLocator.LOGIN_BUTTON[1]))
        self.driver.implicitly_wait(Data.implicitly_wait_time)
        return self.driver
