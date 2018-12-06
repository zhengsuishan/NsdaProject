# -*- coding:utf-8 -*-
# 运行脚本

from appium import webdriver
from AppiumProject.common.init_driver import InitDriver
from AppiumProject.wechat.add_wechat import AddWechat
from AppiumProject.wechat.init_para import InitPara

if __name__ == '__main__':

    #----------------init_para.py文件中修改设备udid，发送的文本内容，需要点击的群坐标----------------------


    desired_caps = InitPara.desired_caps
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    InitDriver.set_driver(InitDriver, driver=driver)
    AddWechat.get_driver(AddWechat)

    AddWechat.go_group(AddWechat)
    AddWechat.select_member(AddWechat)


