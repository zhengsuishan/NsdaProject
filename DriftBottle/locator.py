# -*- coding:utf-8 -*-
# 定位器
from selenium.webdriver.common.by import By

class Locators(object):

    LONIG_FRAME = 'login_frame' #登陆框frame
    ACCOUNT_PASSWORD_BUTTON = (By.XPATH, '//*[@id="switcher_plogin"]') #切换账号密码登录框
    ACCOUNT = (By.XPATH, '//*[@id="u"]') #账号输入框
    PASSWORD = (By.XPATH, '//*[@id="p"]') #密码输入框
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login_button"]') #登录按钮
    MAIN_FRAME = 'mainFrame' #登录后主页的frame
    BOTTLE_BOTTON = (By.XPATH, '//*[@id="TodayInBox"]/li[3]/div/a[2]') #漂流瓶按钮
    BOTTLE_FRAME = 'mainFrame' #进入漂流瓶页面frame
    PUSH_BUTTON = (By.XPATH, '//*[@id="toolbar"]/div/a[1]') #扔一个
    PULL_BUTTON = (By.XPATH, '//*[@id="toolbar"]/div/a[2]') #捞捞看
    MY_BOTTLE_BUTTON = (By.XPATH, '//*[@id="toolbar"]/div/a[3]') #我的瓶子

    #--------------------------------------扔一个瓶子------------------------------------------------
    PT_BOTTLE = (By.XPATH, '//*[@id="bottle_magic"]/div/div[1]/a[1]/p') #普通瓶
    XQ_BUTTLE = (By.XPATH, '//*[@id="bottle_magic"]/div/div[1]/a[2]/p') #心情瓶
    DX_BOTTLE = (By.XPATH, '//*[@id="bottle_magic"]/div/div[1]/a[3]/p') #定向瓶
    ZH_BUTTLE = (By.XPATH, '//*[@id="bottle_magic"]/div/div[1]/a[4]/p') #真话瓶
    TW_BUTTLE = (By.XPATH, '//*[@id="bottle_magic"]/div/div[1]/a[5]/p') #提问瓶
    JW_BUTTLE = (By.XPATH, '//*[@id="bottle_magic"]/div/div[1]/a[6]/p') #交往瓶
    ZY_BUTTLE = (By.XPATH, '//*[@id="bottle_magic"]/div/div[1]/a[7]/p') #祝愿瓶
    CD_BUTTLE = (By.XPATH, '//*[@id="bottle_magic"]/div/div[1]/a[7]/p') #传递瓶

    #---------------------------------------发送消息--------------------------------------------------
    CONTENT = (By.XPATH, '//*[@id="bottle_send"]/div[2]/div[1]/div[4]/div[2]/div[1]/textarea') #内容输入框
    PUSH_SEA_BUTTON = (By.XPATH, '//*[@id="bottle_send"]/div[2]/div[2]/div[3]/a[2]') #扔出去按钮

    #我的瓶子列表页面
    MY_BOTTLE = (By.XPATH, '//*[@id="bottle_all"]/div/div[1]/div/a[1]') #我的瓶子
    BOTTLE_BUTTON = (By.XPATH, '//*[@id="bottle_all"]/div/div[3]/div[1]/div/div[4]/div[1]/p') #瓶子列表
    ANSWER = (By.XPATH, '//*[@id="bottle_mail"]/div[2]/div[2]/div[2]/textarea') #回应输入框
    SEND = (By.XPATH, '//*[@id="bottle_mail"]/div[2]/div[2]/div[3]/a[1]') #发送按钮
    CANCLE = (By.XPATH, '//*[@id="bottle_interactive"]/div/a[1]') #取消按钮