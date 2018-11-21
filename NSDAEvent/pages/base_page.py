# -*- coding:utf-8 -*-
# 页面基类, 所有页面继承此类

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver