# -*- coding:utf-8 -*-
# 登录模块

from  selenium.webdriver.common.by import By

class LoginLocator(object):

    LOGIN_BUTTON = (By.XPATH, '//*[@id="dataHead"]/ul[2]/li/a[1]') #登录按钮
    FRAME_BUTTON = 'fg-layer-iframe1' #登录框的frame
    EMAIL_BUTTON = (By.XPATH, '//*[@id="playeremail"]') #邮箱输入框
    PASSWORD_BUTTON = (By.XPATH, '//*[@id="playerpwd"]') #密码输入框
    LOGIN_BUTTON_CONFIRM_BUTTON = (By.XPATH, '//*[@id="player"]') #登录按钮
    ENTER_INTO_EVENT_BUTTON = (By.XPATH, '//*[@id="lkSetting"]') #进入赛事按钮