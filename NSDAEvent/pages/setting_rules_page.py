# -*- coding:utf-8 -*-
# 赛事规则设置UI操作
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
    action = None

    def get_data(self):
        self.driver = InitDriver.get_driver(InitDriver)
        self.action = InitDriver.get_action(InitDriver)
        self.lodding_time = Data.lodding_wait_time #等待时间
        self.wait_time = Data.wait_time
        self.point_low = Data.point_low #分值区间下限
        self.point_high = Data.point_high #分值区间上限
        self.debate_round_times = Data.DEBATE_ROUND_TIMES #辩论循环赛轮数

    #设置分数区间，勾选允许半分
    def set_points(self):
        self.driver.find_element(EventRulesLocator.DEBATE_EVENT_RULES_SETTING_BUTTON[0], EventRulesLocator.DEBATE_EVENT_RULES_SETTING_BUTTON[1]).click() #点击比赛规则设置按钮
        WebDriverWait(self.driver, self.lodding_time).until(lambda driver:driver.find_element(EventRulesLocator.DEBATE_CYCLE_EVENT_SETTING_BUTTON[0], EventRulesLocator.DEBATE_CYCLE_EVENT_SETTING_BUTTON[1]))
        self.driver.find_element(EventRulesLocator.DEBATE_POINT_FIRST[0], EventRulesLocator.DEBATE_POINT_FIRST[1]).send_keys(self.point_low) #输入分数
        time.sleep(1.0)
        self.driver.find_element(EventRulesLocator.DEBATE_POINTS_SECOND[0], EventRulesLocator.DEBATE_POINTS_SECOND[1]).send_keys(self.point_high) #输入分数
        time.sleep(1.0)
        self.driver.find_element(EventRulesLocator.DEBATE_ALLOW_HALF[0], EventRulesLocator.DEBATE_ALLOW_HALF[1]).click() #点击允许半分按钮
        time.sleep(1.0)

    #设置辩论循环赛轮数
    def set_debate_round(self):
        # 点击添加比赛轮数按钮
        for i in range(0, self.debate_round_times):
            self.driver.find_element(EventRulesLocator.DEBATE_ADD_ROUND[0], EventRulesLocator.DEBATE_ADD_ROUND[1]).click()
            time.sleep(1.0)
        self.action.scroll(100, 300).perform() #滑动页面
        time.sleep(1.0)

        #--------------第一轮--------------------------------------
        self.driver.find_element(EventRulesLocator.ROUND_1_SINGLE_BUTTON[0], EventRulesLocator.ROUND_1_SINGLE_BUTTON[1]).click()
        time.sleep(1.0)
        #-------------第二轮----------------------------
        self.driver.find_element(EventRulesLocator.ROUND_2_SINGLE_BUTTON[0], EventRulesLocator.ROUND_2_SINGLE_BUTTON[1]).click()
        time.sleep(1.0)
        #-----------第三轮--------------------------------
        self.driver.find_element(EventRulesLocator.ROUND_3_MATCH_BUTTON[0], EventRulesLocator.ROUND_3_MATCH_BUTTON[1]).click()
        time.sleep(1.0)
        self.driver.find_element(EventRulesLocator.ROUND_3_MATCH_POWER_BUTTON[0], EventRulesLocator.ROUND_3_MATCH_POWER_BUTTON[1]).click()
        time.sleep(1.0)
        self.driver.find_element(EventRulesLocator.ROUND_3_DOUBLE_BUTTON[0], EventRulesLocator.ROUND_3_DOUBLE_BUTTON[1]).click()
        time.sleep(1.0)
        #-----------第四轮------------------------------------
        self.driver.find_element(EventRulesLocator.ROUND_4_MATCH_BUTTON[0], EventRulesLocator.ROUND_4_MATCH_BUTTON[1]).click()
        time.sleep(1.0)
        self.driver.find_element(EventRulesLocator.ROUND_4_MATCH_POWER_BUTTON[0], EventRulesLocator.ROUND_4_MATCH_POWER_BUTTON[1]).click()
        time.sleep(1.0)
        self.driver.find_element(EventRulesLocator.ROUND_4_DOUBLE_BUTTON[0], EventRulesLocator.ROUND_4_DOUBLE_BUTTON[1]).click()
        time.sleep(1.0)

        self.driver.find_element(EventRulesLocator.SAVE_RULES_BUTTON[0], EventRulesLocator.SAVE_RULES_BUTTON[1]).click()
        time.sleep(3.0)

        #---------------------刷新页面-------------------------
        self.driver.refresh()
        WebDriverWait(self.driver, self.lodding_time).until(lambda driver:driver.find_element(EventRulesLocator.DEBATE_ADD_ROUND[0], EventRulesLocator.DEBATE_ADD_ROUND[1]))
        try:
            WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element(EventRulesLocator.ROUND_5[0], EventRulesLocator.ROUND_5[1]))
            return '循环赛规则设置成功'
        except Exception as e:
            return '循环赛规则设置失败'

    #淘汰赛规则设置
    def





