# -*- coding:utf-8 -*-

from AppiumProject.common.init_driver import InitDriver
from AppiumProject.qq.send_to_qun import SendToQun
from AppiumProject.qq.init_para import InitParm
from appium import webdriver

if __name__ == '__main__':

    desired_caps = InitParm.desired_caps
    driver = driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    InitDriver.set_driver(InitDriver, driver)
    SendToQun.get_driver(SendToQun)
    SendToQun.go_qun_list(SendToQun)
    SendToQun.send(SendToQun)