# -*- coding:utf-8 -*-
# 登录定位器
from selenium.webdriver.common.by import By

class LoginLocator(object):

    EMAIL_INPUT_BOX = (By.XPATH, '//*[@id="txtAccount"]') #邮箱输入框
    PWD_INPUT_BOX = (By.XPATH, '//*[@id="txtPassword"]') #密码输入框
    LOGIN_BUTTON = (By.XPATH, '//*[@id="btnLogin"]') #登录按钮
    ENTER_INTO_EVENT_BUTTON = (By.XPATH, '//*[@id="lkSetting"]') #进入赛事按钮