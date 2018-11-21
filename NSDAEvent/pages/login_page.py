# -*- coding:utf-8 -*-
# 登录页面操作
from NSDAEvent.pages.base_page import BasePage
from NSDAEvent.locators.login_locator import LoginLocator
from NSDAEvent.settings.data import Data
from selenium.webdriver.support.wait import WebDriverWait
from NSDAEvent.locators.event_rules_locator import EventRulesLocator
import time

class LoginPage(BasePage):

    login_email = None
    login_password = None
    lodding_wait_time = None
    wait_time = None

    def get_data(self):
        self.login_email = Data.user_email
        self.login_password = Data.user_password
        self.lodding_wait_time = Data.lodding_wait_time
        self.wait_time = Data.wait_time

    def login(self):
        self.driver.find_element(LoginLocator.LOGIN_BUTTON[0], LoginLocator.LOGIN_BUTTON[1]).click() #点击右上角登录
        self.driver.switch_to.frame(LoginLocator.FRAME_BUTTON)
        time.sleep(0.5)
        self.driver.find_element(LoginLocator.EMAIL_BUTTON[0], LoginLocator.EMAIL_BUTTON[1]).send_keys(self.login_email) #输入邮箱
        time.sleep(0.5)
        self.driver.find_element(LoginLocator.PASSWORD_BUTTON[0], LoginLocator.PASSWORD_BUTTON[1]).send_keys(self.login_password) #输入密码
        time.sleep(0.5)
        self.driver.find_element(LoginLocator.LOGIN_BUTTON_CONFIRM_BUTTON[0], LoginLocator.LOGIN_BUTTON_CONFIRM_BUTTON[1]).click() #点击登录按钮
        WebDriverWait(self.driver, self.lodding_wait_time).until(
            lambda driver: driver.find_element(LoginLocator.ENTER_INTO_EVENT_BUTTON[0],
                                               LoginLocator.ENTER_INTO_EVENT_BUTTON[1]))
        self.driver.find_element(LoginLocator.ENTER_INTO_EVENT_BUTTON[0], LoginLocator.ENTER_INTO_EVENT_BUTTON[1]).click() #点击进入比赛按钮
        try:
            WebDriverWait(self.driver, self.lodding_wait_time).until(lambda driver:driver.find_element(EventRulesLocator.EVENT_TITLE[0], EventRulesLocator.EVENT_TITLE[1]))
            return self.driver.title
        except Exception as e:
            return False