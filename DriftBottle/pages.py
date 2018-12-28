# -*- coding:utf-8 -*-
# UI操作
from DriftBottle.locator import Locators
from DriftBottle.init_driver import InitDriver
from selenium.webdriver.support.wait import WebDriverWait
import time

class LoginPages(object):

    account = '875707618@qq.com'
    password = 'cf.2012'
    net_wait_time = 15
    page_driver = None

    def __init__(self):
        self.page_driver = InitDriver.get_driver(InitDriver)

    def login(self):
        self.page_driver.switch_to.frame(Locators.LONIG_FRAME)
        WebDriverWait(self.page_driver, self.net_wait_time).until(
            lambda driver: driver.find_element(Locators.ACCOUNT_PASSWORD_BUTTON[0],
                                               Locators.ACCOUNT_PASSWORD_BUTTON[1]))
        self.page_driver.find_element(Locators.ACCOUNT_PASSWORD_BUTTON[0], Locators.ACCOUNT_PASSWORD_BUTTON[1]).click()
        time.sleep(1.0)
        text = self.page_driver.find_element(Locators.ACCOUNT[0], Locators.ACCOUNT[1]).get_attribute('text')

        if text == self.account:
            self.page_driver.find_element(Locators.PASSWORD[0], Locators.PASSWORD[1]).send_keys(page_driver)
            time.sleep(1.0)
            self.page_driver.find_element(Locators.LOGIN_BUTTON[0], Locators.LOGIN_BUTTON[1]).click()
            time.sleep(1.0)
            self.page_driver.switch_to.frame(Locators.MAIN_FRAME)
            WebDriverWait(self.page_driver, self.net_wait_time).until(
                lambda driver: driver.find_element(BOTTLE_BOTTON[0], BOTTLE_BOTTON[1]))
            self.page_driver.find_element(Locators.BOTTLE_BOTTON[0], Locators.BOTTLE_BOTTON[1]).click()
            time.sleep(1.0)
            WebDriverWait(self.page_driver, self.net_wait_time).until(
                lambda driver: driver.find_element(Locators.PUSH_BUTTON[0], Locators.PUSH_BUTTON[1]))
        else:
            self.page_driver.find_element(Locators.ACCOUNT[0], Locators.ACCOUNT[1]).send_keys(self.account) #输入账号
            time.sleep(1.0)
            self.page_driver.find_element(Locators.PASSWORD[0], Locators.PASSWORD[1]).send_keys(self.password) #输入密码
            time.sleep(1.0)
            self.page_driver.find_element(Locators.LOGIN_BUTTON[0], Locators.LOGIN_BUTTON[1]).click() #登录
            time.sleep(1.0)
            self.page_driver.switch_to.frame(Locators.MAIN_FRAME)
            WebDriverWait(self.page_driver, self.net_wait_time).until(
                lambda driver: driver.find_element(Locators.BOTTLE_BOTTON[0], Locators.BOTTLE_BOTTON[1]))
            self.page_driver.find_element(Locators.BOTTLE_BOTTON[0], Locators.BOTTLE_BOTTON[1]).click()
            time.sleep(1.0)
            WebDriverWait(self.page_driver, self.net_wait_time).until(lambda driver:driver.find_element(Locators.PUSH_BUTTON[0], Locators.PUSH_BUTTON[1]))

class PushBottle(object):
    net_wait_time = 15
    page_driver = None
    message = '打开支付宝首页搜索“499754”，即可领红包，每天都可以领取哦，支付宝福利，快去试试吧。 '

    def __init__(self):
        self.page_driver = InitDriver.get_driver(InitDriver)

    #扔普通瓶子
    def push_putong_bottle(self):
        temp_bool = True
        while temp_bool:
            try:
                self.page_driver.find_element(Locators.PUSH_BUTTON[0], Locators.PUSH_BUTTON[1]).click()  # 点击扔一个
                temp_bool = False
            except Exception as e:
                if 'not clickable' in str(e):
                    time.sleep(1.0)
        WebDriverWait(self.page_driver, self.net_wait_time).until(lambda driver:driver.find_element(Locators.PT_BOTTLE[0], Locators.PT_BOTTLE[1]))
        self.page_driver.find_element(Locators.PT_BOTTLE[0], Locators.PT_BOTTLE[1]).click() #点击普通瓶
        WebDriverWait(self.page_driver, self.net_wait_time).until(lambda driver:driver.find_element(Locators.CONTENT[0], Locators.CONTENT[1]))
        self.page_driver.find_element(Locators.CONTENT[0], Locators.CONTENT[1]).send_keys(self.message)
        time.sleep(0.5)
        self.page_driver.find_element(Locators.PUSH_SEA_BUTTON[0], Locators.PUSH_SEA_BUTTON[1]).click() #点击扔出去按钮
        time.sleep(3.0)

    #我的瓶子
    def my_bottle(self):
        self.page_driver.find_element(Locators.MY_BOTTLE_BUTTON[0], Locators.MY_BOTTLE_BUTTON[1]).click()
