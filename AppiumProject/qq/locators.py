# -*- coding:utf-8 -*-
# 定位器
from selenium.webdriver.common.by import By

class Locators(object):

    #----------------------------主界面----------------------------
    NEWS = (By.NAME, '消息')
    CONTACT = ('xpath', '')
    LOOK = ('xpath', '')
    DYNAMIC = (By.NAME, '动态')

