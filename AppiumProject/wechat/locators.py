# -*-coding:utf-8 -*-
# 定位器
from selenium.webdriver.common.by import By

class Locators(object):

    #--------------------主界面--------------------
    MAIN_PAGE_WECHAT = (By.NAME, '微信')
    MAIN_PAGE_CONTACT = (By.NAME, '通讯录')
    MAIN_PAGE_FIND = (By.NAME, '发现')
    MAIN_PAGE_ME = (By.NAME, '我')

    #------------------通讯录界面------------------
    CONTACT_PAGE_GROUP_CHAT = (By.NAME, '群聊')

    #------------------群聊列表界面----------------
    GROUP_MEMBER_ID = (By.ID, 'com.tencent.mm:id/dnm')
    GROUP_MEMBER_ALL = (By.NAME, '查看全部群成员')
    GROUP_SEARCH_TEXT = (By.NAME, '搜索')

    #-----------------添加界面----------------------
    ADD_NEWS = (By.NAME, '发消息')
    ADD_CONTACT= (By.NAME, '添加到通讯录')

    #-----------------验证界面------------------
    VARIFY_APPLY = (By.NAME, '验证申请')
    VARIFY_INPUT = (By.ID, 'com.tencent.mm:id/dny')
    VARIFY_SEND = (By.NAME, '发送')

    #-------------------群聊天界面---------------------
    CHAT_RIGHT = (By.ID, 'com.tencent.mm:id/j1')