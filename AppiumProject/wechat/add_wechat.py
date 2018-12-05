# -*- coding:utf-8 -*-
from AppiumProject.common.init_driver import InitDriver
from AppiumProject.wechat.init_para import InitPara
import os
import time
from selenium.webdriver.support.wait import WebDriverWait
from AppiumProject.wechat.locators import Locators

class AddWechat(object):

    driver = None
    udid = InitPara.device_udid
    back_cmd = 'adb -s % shell input keyevent 4'%udid
    number = None
    wait_time = 3
    launch_time = 15
    qun_location_x = InitPara.qun_location_x
    qun_location_y = InitPara.qun_location_y
    click_qun_cmd = 'adb -s %s shell input tap %d %d'%(udid, qun_location_x, qun_location_y)
    swipe_cmd = 'adb -s %s shell input swipe 540 1080 540 1350'%udid

    def get_driver(self):
        self.driver = InitDriver.get_driver(InitDriver)
        self.number = self.read_count(AddWechat)

    def go_group(self):
        WebDriverWait(self.driver, self.launch_time).until(lambda driver: driver.find_element(Locators.MAIN_PAGE_CONTACT[0], Locators.MAIN_PAGE_CONTACT[1]))
        self.driver.find_element(Locators.MAIN_PAGE_CONTACT[0], Locators.MAIN_PAGE_CONTACT[1]).click()
        time.sleep(1.0)
        self.driver.find_element(Locators.CONTACT_PAGE_GROUP_CHAT[0], Locators.CONTACT_PAGE_GROUP_CHAT[1]).click()
        time.sleep(1.0)
        os.popen(self.click_qun_cmd)
        time.sleep(1.0)
        self.driver.find_element(Locators.CHAT_RIGHT[0], Locators.CHAT_RIGHT[1]).click()
        time.sleep(1.0)
        WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element(Locators.GROUP_MEMBER_ID[0], Locators.GROUP_MEMBER_ID[1]))

        while Locators.GROUP_MEMBER_ALL[0] not in self.driver.page_source:
            os.popen(self.swipe_cmd)
            time.sleep(1.0)
        else:
            pass
        driver.find_element(Locators.GROUP_MEMBER_ALL[0], Locators.GROUP_MEMBER_ALL[1]).click()
        WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element(Locators.GROUP_SEARCH_TEXT[0], Locators.GROUP_SEARCH_TEXT[1]))

    def send_verfiy_message(self):
        if Locators.ADD_NEWS[1] in self.driver.page_source:
            os.popen(self.back_cmd)
            time.sleep(1.0)
            self.number += 1
            self.write_count(self.number)
            self.select_member()
        elif Locators.ADD_CONTACT[1] in self.driver.page_source:
            self.driver.find_element(Locators.ADD_CONTACT[0], Locators.ADD_CONTACT[1]).click()
            try:
                WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element(Locators.VARIFY_APPLY[0], Locators.VARIFY_APPLY[1]))
                if InitPara.add_text in self.driver.page_source:
                    self.driver.find_element(Locators.VARIFY_SEND[0], Locators.VARIFY_SEND[1]).click()
                    WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element(Locators.ADD_CONTACT[0], Locators.ADD_CONTACT[1]))
                    os.popen(self.back_cmd)
                    time.sleep(1.0)
                    self.number += 1
                    self.write_count(self.number)
                    self.select_member()
                else:
                    self.driver.find_element(Locators.VARIFY_INPUT[0], Locators.VARIFY_INPUT[1]).clear()
                    time.sleep(1.0)
                    self.driver.find_element(Locators.VARIFY_INPUT[0], Locators.VARIFY_INPUT[1]).send_keys(InitPara.add_text)
                    time.sleep(1.0)
                    self.driver.find_element(Locators.VARIFY_SEND[0], Locators.VARIFY_SEND[1]).click()
                    WebDriverWait(self.driver, self.wait_time).until(
                        lambda driver: driver.find_element(Locators.ADD_CONTACT[0], Locators.ADD_CONTACT[1]))
                    os.popen(self.back_cmd)
                    time.sleep(1.0)
                    self.number += 1
                    self.write_count(self.number)
                    self.select_member()
            except Exception as e:
                if Locators.ADD_NEWS[1] in self.driver.page_source:
                    os.popen(self.back_cmd)
                    time.sleep(1.0)
                    self.number += 1
                    self.write_count(self.number)
                    self.select_member()
                else:
                    raise RuntimeWarning('未知界面')
        else:
            raise RuntimeWarning('未知界面')

    #点击头像
    def select_member(self):
        count = self.read_count(self)
        num1 = int(count/5)                     #用于计算滑动次数
        num2 = int(count%5)                     #用于计算点击那个头像

        if self.udid == '5761c059':

            # --------------滑动到顶部--------------------
            swipe_top_cmd = 'adb -s %s shell input swipe %d %d %d %d %d' % (
            self.udid, InitPara.vivo_swipe_top_x, InitPara.vivo_swipe_top_y1,
            InitPara.vivo_swipe_top_x, InitPara.vivo_swipe_top_y2, InitPara.vivo_swipe_top_time)
            os.popen(swipe_top_cmd)
            time.sleep(1.0)

            for i in range(0, num1):
                swipe_cmd = 'adb -s %s shell input swipe %d %d %d %d %d'%(self.udid, InitPara.vivo_user_swipe_x, InitPara.vivo_user_swipe_y1,
                                                                          InitPara.vivo_user_swipe_x, InitPara.vivo_user_swipe_y2, InitPara.vivo_swipe_time)
                os.popen(swipe_cmd)
                time.sleep(1.0)
            if num2 == 0:
                click_cmd = 'adb -s %s shell input tap %d %d' % (
                self.udid, InitPara.vivo_user_x, InitPara.vivo_user_y)
                os.popen(click_cmd)
                time.sleep(1.0)
            else:
                click_cmd = 'adb -s %s shell input tap %d %d' % (
                self.udid, InitPara.vivo_user_x + InitPara.vivo_user_x_dur * num2, InitPara.vivo_user_y)
                os.popen(click_cmd)
                time.sleep(1.0)
        elif self.udid == 'd102deb37d13':

            # --------------滑动到顶部--------------------
            swipe_top_cmd = 'adb -s %s shell input swipe %d %d %d %d %d' % (
            self.udid, InitPara.xiaomi_swipe_top_x, InitPara.xiaomi_swipe_top_y1,
            InitPara.xiaomi_swipe_top_x, InitPara.xiaomi_swipe_top_y2, InitPara.xiaomi_swipe_top_time)
            os.popen(swipe_top_cmd)
            time.sleep(1.0)

            for i in range(0, num1):
                swipe_cmd = 'adb -s %s shell input swipe %d %d %d %d %d'%(self.udid, InitPara.xiaomi_user_swipe_x, InitPara.xiaomi_user_swipe_y1,
                                                                          InitPara.xiaomi_user_swipe_x, InitPara.xiaomi_user_swipe_y2, InitPara.xiaomi_swipe_time)
                os.popen(swipe_cmd)
                time.sleep(1.0)
            if num2 == 0:
                click_cmd = 'adb -s %s shell input tap %d %d' % (
                self.udid, InitPara.xiaomi_user_x, InitPara.xiaomi_user_y)
                os.popen(click_cmd)
                time.sleep(1.0)
            else:
                click_cmd = 'adb -s %s shell input tap %d %d' % (
                self.udid, InitPara.xiaomi_user_x + InitPara.xiaomi_user_x_dur * num2, InitPara.xiaomi_user_y)
                os.popen(click_cmd)
                time.sleep(1.0)
        else:
            pass

        self.send_verfiy_message(AddWechat)

    def read_count(self):
        file_name = 'C:\\pythonworkspace\\AppiumProject\\wechat\\send_count'
        file = open(file_name).readlines()
        return int(file[0])

    def write_count(self, param):
        file_name = 'C:\\pythonworkspace\\AppiumProject\\wechat\\send_count'
        file = open(file_name, 'w+')
        file.write(param)
        file.close()

if __name__ == '__main__':
    AddWechat.select_member(AddWechat)
