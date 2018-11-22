# -*- coding:utf-8 -*-
# 赛事规则设置
from NSDAEvent.locators.event_rules_locator import EventRulesLocator
from selenium.webdriver.support.wait import WebDriverWait
from NSDAEvent.settings.data import Data
import time

from NSDAEvent.pages.init_driver import InitDriver

class SettingRulesPage(object):

    lodding_time = None
    point_low = None
    point_high = None
    driver = None

    def get_data(self):
        self.lodding_time = Data.lodding_wait_time #等待时间
        self.point_low = Data.point_low #分值区间下限
        self.point_high = Data.point_high #分值区间上限
        self.driver = InitDriver.get_driver(InitDriver)

    def set_points(self):
        self.driver.find_element(EventRulesLocator.DEBATE_EVENT_RULES_SETTING_BUTTON[0], EventRulesLocator.DEBATE_EVENT_RULES_SETTING_BUTTON[1]).click() #点击比赛规则设置按钮
        WebDriverWait(self.driver, self.lodding_time).until(lambda driver:driver.find_element(EventRulesLocator.DEBATE_CYCLE_EVENT_SETTING_BUTTON[0], EventRulesLocator.DEBATE_CYCLE_EVENT_SETTING_BUTTON[1]))
        self.driver.find_element(EventRulesLocator.DEBATE_POINT_FIRST[0], EventRulesLocator.DEBATE_POINT_FIRST[1]).send_keys(self.point_low) #输入分数
        time.sleep(1.0)
        self.driver.find_element(EventRulesLocator.DEBATE_POINTS_SECOND[0], EventRulesLocator.DEBATE_POINTS_SECOND[1]).send_keys(self.point_high) #输入分数
        time.sleep(1.0)
        self.driver.find_element(EventRulesLocator.DEBATE_ALLOW_HALF[0], EventRulesLocator.DEBATE_ALLOW_HALF[1]).click() #点击允许半分按钮

