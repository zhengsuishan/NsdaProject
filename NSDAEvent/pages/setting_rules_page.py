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

    def get_data(self):
        self.driver = InitDriver.get_driver(InitDriver)
        self.action = InitDriver.get_action(InitDriver)
        self.lodding_time = Data.lodding_wait_time #等待时间
        self.wait_time = Data.wait_time
        self.point_low = Data.point_low #分值区间下限
        self.point_high = Data.point_high #分值区间上限
        self.debate_round_times = Data.DEBATE_ROUND_TIMES #辩论循环赛轮数
        self.debate_win_num = Data.DEBATE_WIN_NUM #晋级队伍数
        self.success_promote = Data.SUCCESS_PTOMOTE #把比赛时间设置为今天提示

    #设置分数区间，勾选允许半分
    def set_points(self):
        self.driver.find_element(EventRulesLocator.DEBATE_EVENT_RULES_SETTING_BUTTON[0], EventRulesLocator.DEBATE_EVENT_RULES_SETTING_BUTTON[1]).click() #点击比赛规则设置按钮
        WebDriverWait(self.driver, self.lodding_time).until(lambda driver:driver.find_element(EventRulesLocator.DEBATE_CYCLE_EVENT_SETTING_BUTTON[0], EventRulesLocator.DEBATE_CYCLE_EVENT_SETTING_BUTTON[1]))

        self.driver.execute_script('window.scrollTo(0, 300);')  # 滑动页面
        time.sleep(1.0)

        try:
            WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element(EventRulesLocator.ROUND_4_MATCH_BUTTON[0], EventRulesLocator.ROUND_4_MATCH_BUTTON[1]))
            pass
        except Exception as e:
            self.driver.find_element(EventRulesLocator.DEBATE_POINT_FIRST[0],
                                     EventRulesLocator.DEBATE_POINT_FIRST[1]).clear()  # 清空输入框
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.DEBATE_POINT_FIRST[0],
                                     EventRulesLocator.DEBATE_POINT_FIRST[1]).send_keys(self.point_low)  # 输入分数
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.DEBATE_POINTS_SECOND[0],
                                     EventRulesLocator.DEBATE_POINTS_SECOND[1]).clear()
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.DEBATE_POINTS_SECOND[0],
                                     EventRulesLocator.DEBATE_POINTS_SECOND[1]).send_keys(self.point_high)  # 输入分数
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.DEBATE_ALLOW_HALF[0],
                                     EventRulesLocator.DEBATE_ALLOW_HALF[1]).click()  # 点击允许半分按钮
            time.sleep(1.0)

    #设置辩论循环赛轮数
    def set_debate_round(self):
        # --------------------------------先判断是否设置过规则---------------------------------
        try:
            WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element(EventRulesLocator.ROUND_4_MATCH_BUTTON[0], EventRulesLocator.ROUND_4_MATCH_BUTTON[1]))
            pass
        except Exception as e:
            # 点击添加比赛轮数按钮
            for i in range(0, self.debate_round_times):
                self.driver.find_element(EventRulesLocator.DEBATE_ADD_ROUND[0],
                                         EventRulesLocator.DEBATE_ADD_ROUND[1]).click()
                time.sleep(1.0)

            # --------------第一轮--------------------------------------
            self.driver.find_element(EventRulesLocator.ROUND_1_SINGLE_BUTTON[0],
                                     EventRulesLocator.ROUND_1_SINGLE_BUTTON[1]).click()
            time.sleep(1.0)
            # -------------第二轮----------------------------
            self.driver.find_element(EventRulesLocator.ROUND_2_SINGLE_BUTTON[0],
                                     EventRulesLocator.ROUND_2_SINGLE_BUTTON[1]).click()
            time.sleep(1.0)
            # -----------第三轮--------------------------------
            self.driver.find_element(EventRulesLocator.ROUND_3_MATCH_BUTTON[0],
                                     EventRulesLocator.ROUND_3_MATCH_BUTTON[1]).click()
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.ROUND_3_MATCH_POWER_BUTTON[0],
                                     EventRulesLocator.ROUND_3_MATCH_POWER_BUTTON[1]).click()
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.ROUND_3_DOUBLE_BUTTON[0],
                                     EventRulesLocator.ROUND_3_DOUBLE_BUTTON[1]).click()
            time.sleep(1.0)
            # -----------第四轮------------------------------------
            self.driver.find_element(EventRulesLocator.ROUND_4_MATCH_BUTTON[0],
                                     EventRulesLocator.ROUND_4_MATCH_BUTTON[1]).click()
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.ROUND_4_MATCH_POWER_BUTTON[0],
                                     EventRulesLocator.ROUND_4_MATCH_POWER_BUTTON[1]).click()
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.ROUND_4_DOUBLE_BUTTON[0],
                                     EventRulesLocator.ROUND_4_DOUBLE_BUTTON[1]).click()
            time.sleep(1.0)

            self.driver.find_element(EventRulesLocator.SAVE_RULES_BUTTON[0],
                                     EventRulesLocator.SAVE_RULES_BUTTON[1]).click()
            time.sleep(3.0)

            # ---------------------刷新页面-------------------------
            self.driver.refresh()
            WebDriverWait(self.driver, self.lodding_time).until(
                lambda driver: driver.find_element(EventRulesLocator.DEBATE_ADD_ROUND[0],
                                                   EventRulesLocator.DEBATE_ADD_ROUND[1]))
            try:
                WebDriverWait(self.driver, self.wait_time).until(
                    lambda driver: driver.find_element(EventRulesLocator.ROUND_5[0], EventRulesLocator.ROUND_5[1]))
                return '循环赛规则设置成功'
            except Exception as e:
                return '循环赛规则设置失败'

        self.driver.execute_script('window.scrollTo(300, 0);')  # 滑动页面
        time.sleep(1.0)

    #淘汰赛规则设置
    def set_out(self):
        self.driver.find_element(EventRulesLocator.DEBATE_OUT_EVENT_SETTING_BUTTON[0], EventRulesLocator.DEBATE_OUT_EVENT_SETTING_BUTTON[1]).click() #点击淘汰赛设置按钮
        WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element(EventRulesLocator.DEBATE_WIN_NUMBER[0], EventRulesLocator.DEBATE_WIN_NUMBER[1]))

        #--------------------------------先判断是否设置过规则---------------------------------
        self.driver.execute_script('window.scrollTo(0, 200);')  # 滑动页面
        time.sleep(1.0)
        try:
            WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element(EventRulesLocator.FINALS_JUDGMENT[0], EventRulesLocator.FINALS_JUDGMENT[1]))
            pass
        except Exception as e:
            self.driver.find_element(EventRulesLocator.DEBATE_WIN_NUMBER[0],
                                     EventRulesLocator.DEBATE_WIN_NUMBER[1]).clear()  # 清空输入框
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.DEBATE_WIN_NUMBER[0],
                                     EventRulesLocator.DEBATE_WIN_NUMBER[1]).send_keys(self.debate_win_num)  # 输入晋级队伍数量
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.DEBATE_CONFIRM_BUTTON[0],
                                     EventRulesLocator.DEBATE_CONFIRM_BUTTON[1]).click()  # 点击保存晋级队伍按钮

            # ------------------------------Partial--------------------------------
            self.driver.find_element(EventRulesLocator.PARTIAL_JUDGMENT[0],
                                     EventRulesLocator.PARTIAL_JUDGMENT[1]).clear()
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.PARTIAL_JUDGMENT[0],
                                     EventRulesLocator.PARTIAL_JUDGMENT[1]).send_keys(3) #数日裁判数量
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.PARTIAL_SINGLE_BUTTON[0],
                                     EventRulesLocator.PARTIAL_SINGLE_BUTTON[1]).click()
            time.sleep(1.0)

            # ------------------------------Quarterfinals--------------------------------
            self.driver.find_element(EventRulesLocator.QUARTERFINALS_JUDGMENT[0],
                                     EventRulesLocator.QUARTERFINALS_JUDGMENT[1]).clear()
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.QUARTERFINALS_JUDGMENT[0],
                                     EventRulesLocator.QUARTERFINALS_JUDGMENT[1]).send_keys(3) #数日裁判数量
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.QUARTERFINALS_SINGLE_BUTTON[0],
                                     EventRulesLocator.QUARTERFINALS_SINGLE_BUTTON[1]).click()
            time.sleep(1.0)

            # ------------------------------Semifinals--------------------------------
            self.driver.find_element(EventRulesLocator.SEMIFINALS_JUDGMENT[0],
                                     EventRulesLocator.SEMIFINALS_JUDGMENT[1]).clear()
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.SEMIFINALS_JUDGMENT[0],
                                     EventRulesLocator.SEMIFINALS_JUDGMENT[1]).send_keys(5) #数日裁判数量
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.SEMIFINALS_SINGLE_BUTTON[0],
                                     EventRulesLocator.SEMIFINALS_SINGLE_BUTTON[1]).click()
            time.sleep(1.0)

            # ------------------------------Finals--------------------------------
            self.driver.find_element(EventRulesLocator.FINALS_JUDGMENT[0], EventRulesLocator.FINALS_JUDGMENT[1]).clear()
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.FINALS_JUDGMENT[0], EventRulesLocator.FINALS_JUDGMENT[1]).send_keys(7) #数日裁判数量
            time.sleep(1.0)
            self.driver.find_element(EventRulesLocator.FINALS_SINGLE_BUTTON[0],
                                     EventRulesLocator.FINALS_SINGLE_BUTTON[1]).click()
            time.sleep(1.0)

            #------------------------------保存--------------------------------------
            self.driver.find_element(EventRulesLocator.SAVE_BUTTON[0], EventRulesLocator.SAVE_BUTTON[1]).click()  # 保存规则
            time.sleep(3.0)

            #-------------------------------判断是否保存成功----------------------
            self.driver.refresh()
            WebDriverWait(self.driver, self.wait_time).until(lambda driver:driver.find_element(EventRulesLocator.DEBATE_WIN_NUMBER[0], EventRulesLocator.DEBATE_WIN_NUMBER[1]))
            try:
                WebDriverWait(self.driver, self.wait_time).until(
                    lambda driver: driver.find_element(EventRulesLocator.FINALS_JUDGMENT[0],
                                                       EventRulesLocator.FINALS_JUDGMENT[1]))
                return '淘汰赛规则设置成功'
            except Exception as e:
                return '淘汰赛规则设置失败'

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








