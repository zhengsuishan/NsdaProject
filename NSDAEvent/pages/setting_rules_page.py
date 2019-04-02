# -*- coding:utf-8 -*-
# 赛事规则设置UI操作
from NSDAEvent.locators.event_rules_locator import EventRulesLocator
from selenium.webdriver.support.wait import WebDriverWait
from NSDAEvent.settings.data import Data
import time
from NSDAEvent.pages.init_driver import InitDriver
from selenium.webdriver.common.by import By

class SettingRulesPage(object):

    lodding_time = None
    point_low = None
    point_high = None
    driver = None
    action = None
    sleep_time = None
    event_type = None

    def get_data(self):
        self.driver = InitDriver.get_driver(InitDriver)
        self.action = InitDriver.get_action(InitDriver)
        self.lodding_time = Data.lodding_wait_time #等待时间
        self.wait_time = Data.wait_time
        self.point_low = Data.point_low #分值区间下限
        self.point_high = Data.point_high #分值区间上限
        self.debate_round_times = Data.DEBATE_ROUND #辩论循环赛轮数
        self.debate_win_num = Data.DEBATE_WIN_NUM #晋级队伍数
        self.success_promote = Data.SUCCESS_PTOMOTE #把比赛时间设置为今天提示
        self.sleep_time = Data.sleep_time #UI操作等待时间
        self.event_type = Data.event_type #赛事类型
        self.match_list = Data.MATCH_LIST #匹配方式
        self.flight_list = Data.FLISHT_LIST #flight类型

    #设置分数区间，勾选允许半分
    def set_points(self):

        if self.event_type == 1:
            self.driver.find_element(EventRulesLocator.DEBATE_EVENT_RULES_SETTING_BUTTON[0],
                                     EventRulesLocator.DEBATE_EVENT_RULES_SETTING_BUTTON[1]).click()  # 点击比赛规则设置按钮
            time.sleep(self.sleep_time)
            WebDriverWait(self.driver, self.lodding_time).until(
                lambda driver: driver.find_element(EventRulesLocator.DEBATE_CYCLE_EVENT_SETTING_BUTTON[0],
                                                   EventRulesLocator.DEBATE_CYCLE_EVENT_SETTING_BUTTON[1]))

            self.driver.execute_script('window.scrollTo(0, 300);')  # 滑动页面
            time.sleep(self.sleep_time)
            self.driver.find_element(EventRulesLocator.DEBATE_POINT_FIRST[0],
                                     EventRulesLocator.DEBATE_POINT_FIRST[1]).clear()  # 清空输入框
            time.sleep(self.sleep_time)
            self.driver.find_element(EventRulesLocator.DEBATE_POINT_FIRST[0],
                                     EventRulesLocator.DEBATE_POINT_FIRST[1]).send_keys(self.point_low)  # 输入分数
            time.sleep(self.sleep_time)
            self.driver.find_element(EventRulesLocator.DEBATE_POINTS_SECOND[0],
                                     EventRulesLocator.DEBATE_POINTS_SECOND[1]).clear()
            time.sleep(self.sleep_time)
            self.driver.find_element(EventRulesLocator.DEBATE_POINTS_SECOND[0],
                                     EventRulesLocator.DEBATE_POINTS_SECOND[1]).send_keys(self.point_high)  # 输入分数
            time.sleep(self.sleep_time)
            self.driver.find_element(EventRulesLocator.DEBATE_ALLOW_HALF[0],
                                     EventRulesLocator.DEBATE_ALLOW_HALF[1]).click()  # 点击允许半分按钮
            time.sleep(self.sleep_time)

        elif self.event_type == 2:
            pass
        else:
            raise '请检查赛事类型'


    #设置辩论循环赛轮数
    def set_debate_round(self):

        if self.event_type == 1:
            # 点击添加比赛轮数按钮
            for i in range(0, self.debate_round_times):
                self.driver.find_element(EventRulesLocator.DEBATE_ADD_ROUND[0],
                                         EventRulesLocator.DEBATE_ADD_ROUND[1]).click()
                time.sleep(self.sleep_time)
            # 设置每轮循环赛匹配规则和flight类型
            for round in range(0, self.debate_round_times):
                self.driver.find_element(EventRulesLocator.ROUND_MATCH_BUTTON[0],
                                         EventRulesLocator.ROUND_MATCH_BUTTON[1] % (round + 1)).click()
                time.sleep(self.sleep_time)
                self.driver.find_element(EventRulesLocator.ROUND_MATCH_TYPE_BUTTON[0],
                                         EventRulesLocator.ROUND_MATCH_TYPE_BUTTON[1] % (
                                         round + 1, self.match_list[round])).click()
                time.sleep(self.sleep_time)
                self.driver.find_element(EventRulesLocator.ROUND_FLIGHT_BUTTON[0],
                                         EventRulesLocator.ROUND_FLIGHT_BUTTON[1] % (
                                         round + 1, self.flight_list[round])).click()
                time.sleep(self.sleep_time)

            # 保存设置
            self.driver.find_element(EventRulesLocator.SAVE_RULES_BUTTON[0],
                                         EventRulesLocator.SAVE_RULES_BUTTON[1]).click()
            time.sleep(self.lodding_time)
        elif self.event_type == 2:
            pass
        else:
            raise '赛事类型错误'

    #淘汰赛规则设置
    def set_out(self):
        self.driver.find_element(EventRulesLocator.DEBATE_OUT_EVENT_SETTING_BUTTON[0], EventRulesLocator.DEBATE_OUT_EVENT_SETTING_BUTTON[1]).click() #点击淘汰赛设置按钮

        #根据晋级队伍计算应该生成几轮比赛
        if self.debate_win_num <= 2:
            self.debate_win_num = 2
        elif 2 < self.debate_win_num <=4:
            self.debate_win_num = 4
        elif 4 < self.debate_win_num <= 8:
            self.debate_win_num = 8
        elif 8 < self.debate_win_num <= 16:
            self.debate_win_num = 16
        elif 16 < self.debate_win_num <= 32:
            self.debate_win_num = 32
        elif 32 < self.debate_win_num <= 64:
            self.debate_win_num = 64
        else:
            raise '请检查晋级队伍数'




    #临时吧比赛日期设为今天
    def temp_set_day(self):
        self.driver.find_element(EventRulesLocator.DEBATE_CYCLE_EVENT_SETTING_BUTTON[0],
                                 EventRulesLocator.DEBATE_CYCLE_EVENT_SETTING_BUTTON[1]).click()
        WebDriverWait(self.driver, self.wait_time).until(
            lambda driver: driver.find_element(EventRulesLocator.DEBATE_TEMP_SETTING_EVENT_DAY[0],
                                               EventRulesLocator.DEBATE_TEMP_SETTING_EVENT_DAY[1]))
        self.driver.find_element(EventRulesLocator.DEBATE_TEMP_SETTING_EVENT_DAY[0],
                                 EventRulesLocator.DEBATE_TEMP_SETTING_EVENT_DAY[1]).click()  # 点击临时把比赛设为今天按钮
        time.sleep(1.5)

        if self.driver.switch_to.alert.text == self.success_promote:
            alert = self.driver.switch_to.alert
            alert.accept()
            return '成功临时把比赛时间设为当天'
        else:
            return '失败临时把比赛时间设为当天'








