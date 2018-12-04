# -*- coding:utf-8 -*-
# 组织测试用例，运行测试用例前初始化driver

from selenium import webdriver
from NSDAEvent.settings.data import Data
from selenium.webdriver.support.wait import WebDriverWait
from NSDAEvent.locators.login_locator import LoginLocator
from NSDAEvent.pages.init_driver import InitDriver

import unittest
from NSDAEvent.cases.login import Login
from NSDAEvent.cases.rules import Rules
from NSDAEvent.cases.judge import Judge
from NSDAEvent.cases.room import Room

if __name__ == '__main__':
    wait_time = Data.wait_time
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Data.url)
    WebDriverWait(driver, wait_time).until(
        lambda driver: driver.find_element(LoginLocator.LOGIN_BUTTON[0], LoginLocator.LOGIN_BUTTON[1]))
    driver.implicitly_wait(Data.implicitly_wait_time)

    action = webdriver.TouchActions(driver)

    InitDriver.set_driver(InitDriver, driver=driver)
    InitDriver.set_action(InitDriver, action=action)

    #-----------------------------执行测试用例----------------------------------------------------
    suite_login = unittest.TestLoader().loadTestsFromTestCase(Login) #登录赛事管理员
    suite_rules = unittest.TestLoader().loadTestsFromTestCase(Rules) #设置比赛规则
    suite_judge = unittest.TestLoader().loadTestsFromTestCase(Judge) #添加裁判测试用例
    suite_room = unittest.TestLoader().loadTestsFromTestCase(Room) #添加教室测试用例

    suite = unittest.TestSuite([suite_login, suite_rules, suite_judge, suite_room])

    unittest.TextTestRunner(verbosity=2).run(suite)

    driver.close() #关闭浏览器