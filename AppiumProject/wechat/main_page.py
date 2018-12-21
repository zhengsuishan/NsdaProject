# -*-coding:utf-8-*-
# 从其他界面返回主界面
from AppiumProject.wechat.init_para import InitPara
from AppiumProject.wechat.locators import Locators
from AppiumProject.common.init_driver import InitDriver
import time
import os

class MainPage(object):

    driver = None
    udid = InitPara.device_udid
    back_cmd = 'adb -s %s shell input keyevent 4' % udid
    wake_cmd ='adb -s %s shell am start com.tencent.mm/.ui.LauncherUI'%udid

    def get_driver(self):
        self.driver = InitDriver.get_driver(InitDriver)

    def element(self, locator):
        try:
            self.driver.find_element(locator[0], locator[1])
            return True
        except Exception as e:
            return False

    def back_main_page(self):
        if '微信' in self.driver.page_source and '通讯录' in self.driver.page_source and '发现' in self.driver.page_source and '我' in self.driver.page_source:
            self.driver.find_element(Locators.MAIN_PAGE_WECHAT[0], Locators.MAIN_PAGE_WECHAT[1]).click()
            time.sleep(1.0)
        elif '新的朋友' in self.driver.page_source and '群聊' in self.driver.page_source and '标签' in self.driver.page_source and '公众号' in self.driver.page_source:
            self.driver.find_element(Locators.MAIN_PAGE_WECHAT[0], Locators.MAIN_PAGE_WECHAT[1]).click()
            time.sleep(1.0)
        elif '群聊' in self.driver.page_source and '新的朋友' not in self.driver.page_source:
            os.popen(self.back_cmd)
            time.sleep(1.0)
            self.driver.find_element(Locators.MAIN_PAGE_WECHAT[0], Locators.MAIN_PAGE_WECHAT[1]).click()
            time.sleep(1.0)
        elif self.element(MainPage, Locators.CHAT_RIGHT):
            os.popen(self.back_cmd)
            time.sleep(1.0)
        elif self.element(MainPage, Locators.GROUP_MEMBER_ID):
            os.popen(self.back_cmd)
            time.sleep(1.0)
            os.popen(self.back_cmd)
            time.sleep(1.0)
        elif '查看全部群成员' in self.driver.page_source:
            os.popen(self.back_cmd)
            time.sleep(1.0)
            os.popen(self.back_cmd)
            time.sleep(1.0)
        elif '搜索' in self.driver.page_source:
            os.popen(self.back_cmd)
            time.sleep(1.0)
            os.popen(self.back_cmd)
            time.sleep(1.0)
            os.popen(self.back_cmd)
            time.sleep(1.0)
        elif '添加到通讯录' in self.driver.page_source:
            os.popen(self.back_cmd)
            time.sleep(1.0)
            self.back_main_page(MainPage)
        elif '发消息' in self.driver.page_source:
            os.popen(self.back_cmd)
            time.sleep(1.0)
            self.back_main_page(MainPage)
        elif '你需要发送验证申请，等对方通过' in self.driver.page_source:
            os.popen(self.back_cmd)
            time.sleep(1.0)
            self.back_main_page(MainPage)
        elif '由于对方的隐私设置，你无法通过群聊将其添加至通讯录。' in self.driver.page_source:
            os.popen(self.back_cmd)
            time.sleep(1.0)
            self.back_main_page(MainPage)
        else:
            os.popen(self.wake_cmd)
            time.sleep(1.0)
            self.back_main_page(MainPage)