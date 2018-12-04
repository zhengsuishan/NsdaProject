# -*- coding:utf-8 -*-
# 初始化driver， 提供get_driver方法, d定位元素方法

class InitDriver(object):

    driver = None

    def set_driver(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver