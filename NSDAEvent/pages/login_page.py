# -*- coding:utf-8 -*-
# 登录页面UI操作

from NSDAEvent.locators.login_locator import LoginLocator
from NSDAEvent.settings.data import Data
from selenium.webdriver.support.wait import WebDriverWait
from NSDAEvent.locators.event_rules_locator import EventRulesLocator
import time
from NSDAEvent.pages.init_driver import InitDriver
from NSDAEvent.common.save_pic import SavePic

class LoginPage(object):

    login_email = None
    login_password = None
    lodding_wait_time = None
    wait_time = None
    driver = None

    def get_data(self):
        self.login_email = Data.user_email #读取登录邮箱
        self.login_password = Data.user_password #读取登陆密码
        self.lodding_wait_time = Data.lodding_wait_time #读取等待时间
        self.wait_time = Data.wait_time #读取等待时间
        self.sleep_time = Data.sleep_time #ui操作间隔
        self.driver = InitDriver.get_driver(InitDriver)

    def login(self):
        self.driver.find_element(LoginLocator.EMAIL_INPUT_BOX[0], LoginLocator.EMAIL_INPUT_BOX[1]).send_keys(self.login_email) #输入邮箱
        time.sleep(self.sleep_time)
        self.driver.find_element(LoginLocator.PWD_INPUT_BOX[0], LoginLocator.PWD_INPUT_BOX[1]).send_keys(self.login_password) #输入密码
        time.sleep(self.sleep_time)
        self.driver.find_element(LoginLocator.LOGIN_BUTTON[0], LoginLocator.LOGIN_BUTTON[1]).click() #点击登录按钮
        WebDriverWait(self.driver, self.lodding_wait_time).until(
            lambda driver: driver.find_element(LoginLocator.ENTER_INTO_EVENT_BUTTON[0],
                                               LoginLocator.ENTER_INTO_EVENT_BUTTON[1]))
        self.driver.find_element(LoginLocator.ENTER_INTO_EVENT_BUTTON[0], LoginLocator.ENTER_INTO_EVENT_BUTTON[1]).click() #点击进入比赛按钮
        try:
            WebDriverWait(self.driver, self.lodding_wait_time).until(lambda driver:driver.find_element(EventRulesLocator.EVENT_TITLE[0], EventRulesLocator.EVENT_TITLE[1]))
            return self.driver.title
        except Exception as e:
            SavePic().get_pic(self.driver)