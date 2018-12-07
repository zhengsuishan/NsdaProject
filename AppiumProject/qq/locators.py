# -*- coding:utf-8 -*-
# 定位器
from selenium.webdriver.common.by import By

class Locators(object):

    #----------------------------主界面----------------------------
    NEWS = (By.NAME, '消息')
    CONTACT = (By.NAME, '联系人')
    LOOK = (By.NAME, '看点')
    DYNAMIC = (By.NAME, '动态')
    QUN_NAME_ID = (By.ID, 'com.tencent.mobileqq:id/text1')
    PIC = (By.ID, 'com.tencent.mobileqq:id/name')
    SLIENT = (By.NAME, '全员禁言中')
    SENG_INPUT = (By.ID, 'com.tencent.mobileqq:id/input')
    SEND_THREE = (By.NAME, '发送(3)')
    SEND_TWO = (By.NAME, '发送(2)')
    SEND_ONE = (By.NAME, '发送(1)')
    SEND = (By.NAME, '发送')
    RIGHT_ID = (By.ID, 'com.tencent.mobileqq:id/ivTitleBtnRightImage')
    XIANG_CE = (By.NAME, '相册')
    BIAN_JI = (By.NAME, '编辑')
    YUAN_TU = (By.NAME, '原图')

