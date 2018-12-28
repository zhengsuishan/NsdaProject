# -*- coding:utf-8 -*-
# 初始化driver
from selenium import webdriver

class InitDriver(object):

    driver = None

    def set_driver(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver