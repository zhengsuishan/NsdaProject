# -*- coding:utf-8 -*-
# 加群UI操作

from AppiumProject.common.init_driver import InitDriver
from AppiumProject.qq.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
import time

class AddGroup(object):

    driver = None

    def get_driver(self):
        self.driver = InitDriver.get_driver(InitDriver)

    def search(self):
        time.sleep(15.0)
        self.driver.find_element(Locators.DYNAMIC[0], Locators.DYNAMIC[1]).click()


if __name__ == '__main__':
    pass

