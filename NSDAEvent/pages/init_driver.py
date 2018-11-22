# -*- coding:utf-8 -*-
# 在run.py文件，运行测试用例前初始化driver，提供get_driver方法获取driver对象

class InitDriver(object):

    driver = None

    def set_driver(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver
