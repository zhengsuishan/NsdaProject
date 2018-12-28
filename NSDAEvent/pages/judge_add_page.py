# -*- coding:utf-8 -*-
# 添加裁判UI操作

from NSDAEvent.locators.judge_locator import JudgeLocator
from NSDAEvent.pages.init_driver import InitDriver
from NSDAEvent.settings.data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

class JudgeAddPage(object):

    driver = None
    wait_time = None

    def get_data(self):
        self.driver = InitDriver.get_driver(InitDriver)
        self.wait_time = Data.wait_time
        self.judge_number = JudgeLocator.JUDGE_NAME_LIST.__len__()

    def add_judge(self):
        self.driver.find_element(JudgeLocator.JUDGE_BUTTON[0], JudgeLocator.JUDGE_BUTTON[1]).click() #点击裁判报名管理按钮
        time.sleep(1.0)

        for index in range(0, self.judge_number):
            self.driver.find_element(JudgeLocator.JUDGE_ADD_BUTTON[0],
                                     JudgeLocator.JUDGE_ADD_BUTTON[1]).click()  # 点击临时添加裁判按钮
            time.sleep(1.0)
            # 切换frame
            self.driver.switch_to.frame('fg-layer-iframe1')
            time.sleep(1.0)
            #输入裁判姓名
            self.driver.find_element(JudgeLocator.JUDGE_NAME[0], JudgeLocator.JUDGE_NAME[1]).send_keys(
                JudgeLocator.JUDGE_NAME_LIST[index])
            time.sleep(1.0)
            #输入裁判手机号
            self.driver.find_element(JudgeLocator.JUDGE_PHONE[0], JudgeLocator.JUDGE_PHONE[1]).send_keys(
                JudgeLocator.JUDGE_PHONE_LIST[index])
            time.sleep(1.0)
            #点击省份
            self.driver.find_element(JudgeLocator.JUDGE_PROVINCE[0], JudgeLocator.JUDGE_PROVINCE[1]).click()
            time.sleep(1.0)
            #选择省份
            Select(self.driver.find_element(JudgeLocator.JUDGE_PROVINCE[0],
                                            JudgeLocator.JUDGE_PROVINCE[1])).select_by_visible_text(JudgeLocator.JUDGE_PROVINCE_LIST[index])
            time.sleep(1.0)
            self.driver.find_element(JudgeLocator.JUDGE_CITY[0], JudgeLocator.JUDGE_CITY[1]).click()
            time.sleep(1.0)
            #选择市区
            Select(self.driver.find_element(JudgeLocator.JUDGE_CITY[0], JudgeLocator.JUDGE_CITY[1])).select_by_visible_text(JudgeLocator.JUDGE_CITY_LIST[index])
            time.sleep(1.0)
            self.driver.find_element(JudgeLocator.JUDGE_SCHOOL[0], JudgeLocator.JUDGE_SCHOOL[1]).click()
            time.sleep(1.0)
            #选择学校
            Select(self.driver.find_element(JudgeLocator.JUDGE_SCHOOL[0], JudgeLocator.JUDGE_SCHOOL[1])).select_by_visible_text(JudgeLocator.JUDGE_SCHOOL_LIST[index])
            time.sleep(1.0)
            self.driver.find_element(JudgeLocator.JUDGE_CONFIRM_BUTTON[0], JudgeLocator.JUDGE_CONFIRM_BUTTON[1]).click()
            time.sleep(1.0)