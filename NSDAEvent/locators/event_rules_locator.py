# -*- coding:utf-8 -*-
# 比赛规则设置定位器
from selenium.webdriver.common.by import By

class EventRulesLocator(object):

    EVENT_TITLE = (By.TAG_NAME, 'h3') #赛事标题

    #--------------------------------辩论赛事,循环赛规则设置--------------------------------------
    DEBATE_EVENT_RULES_SETTING_BUTTON = (By.XPATH, '//*[@id="lkRuleSettings"]/p') #比赛规则设置按钮
    DEBATE_CYCLE_EVENT_SETTING_BUTTON = (By.XPATH, '/html/body/div[3]/div[2]/div[1]/a[1]') #循环赛规则设置按钮
    DEBATE_TEMP_SETTING_EVENT_DAY = (By.ID, 'btnAdminSetDate') #临时把比赛日期设置为今天按钮
    DEBATE_POINT_FIRST = (By.XPATH, '//*[@id="data"]/div/div[1]/input[1]') #分值区间输入框
    DEBATE_POINTS_SECOND = (By.XPATH, '//*[@id="data"]/div/div[1]/input[2]') #分值区间输入框
    DEBATE_ALLOW_HALF = (By.XPATH, '//*[@id="data"]/div/div[2]/label[2]/input') #允许打半分按钮
    DEBATE_DENY_HALF = (By.XPATH, '//*[@id="data"]/div/div[2]/label[3]/input') #不允许打半分按钮
    DEBATE_ADD_ROUND = (By.XPATH, '//*[@id="data"]/div/div[3]/a') #添加比赛轮数按钮

    ROUND_1_MATCH_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[1]/div[1]/select') #循环赛第一轮匹配方式按钮
    ROUND_1_MATCH_RANDOM_BUTTON =(By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[1]/div[1]/select/option[1]') #循环赛第一轮随机匹配按钮
    ROUND_1_MATCH_POWER_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[1]/div[1]/select/option[2]') #循环赛第一轮实力匹配按钮
    ROUND_1_SINGLE_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[1]/div[2]/label') #循环赛第一轮SINGLE FLIGHT按钮
    ROUND_1_DOUBLE_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[1]/div[3]/label') #循环赛第一轮DOUBLE FLIGHT按钮
    ROUND_1_TRIPLE_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[1]/div[4]/label') #循环赛第一轮TRIPE FLIGHT按钮

    ROUND_2_MATCH_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[2]/div[1]/select')  # 循环赛第二轮匹配方式按钮
    ROUND_2_MATCH_RANDOM_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[2]/div[1]/select/option[1]')  # 循环赛第二轮随机匹配按钮
    ROUND_2_MATCH_POWER_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[2]/div[1]/select/option[2]')  # 循环赛第二轮实力匹配按钮
    ROUND_2_SINGLE_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[2]/div[2]/label')  # 循环赛第二轮SINGLE FLIGHT按钮
    ROUND_2_DOUBLE_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[2]/div[3]/label')  # 循环赛第二轮DOUBLE FLIGHT按钮
    ROUND_2_TRIPLE_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[2]/div[4]/label')  # 循环赛第二轮TRIPE FLIGHT按钮

    ROUND_3_MATCH_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[3]/div[1]/select')  # 循环赛第三轮匹配方式按钮
    ROUND_3_MATCH_RANDOM_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[3]/div[1]/select/option[1]')  # 循环赛第三轮随机匹配按钮
    ROUND_3_MATCH_POWER_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[3]/div[1]/select/option[2]')  # 循环赛第三轮实力匹配按钮
    ROUND_3_SINGLE_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[3]/div[2]/label')  # 循环赛第三轮SINGLE FLIGHT按钮
    ROUND_3_DOUBLE_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[3]/div[3]/label')  # 循环赛第三轮DOUBLE FLIGHT按钮
    ROUND_3_TRIPLE_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[3]/div[4]/label')  # 循环赛第三轮TRIPE FLIGHT按钮

    ROUND_4_MATCH_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[4]/div[1]/select')  # 循环赛第四轮匹配方式按钮
    ROUND_4_MATCH_RANDOM_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[4]/div[1]/select/option[1]')  # 循环赛第四轮随机匹配按钮
    ROUND_4_MATCH_POWER_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[4]/div[1]/select/option[2]')  # 循环赛第四轮实力匹配按钮
    ROUND_4_SINGLE_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[4]/div[2]/label')  # 循环赛第四轮SINGLE FLIGHT按钮
    ROUND_4_DOUBLE_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[4]/div[3]/label')  # 循环赛第四轮DOUBLE FLIGHT按钮
    ROUND_4_TRIPLE_BUTTON = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[4]/div[4]/label')  # 循环赛第四轮TRIPE FLIGHT按钮

    ROUND_5 = (By.XPATH, '//*[@id="data"]/div/div[4]/ul/li[5]/div[1]/label') #循环赛第五轮，用户判断规则是否设置成功

    SAVE_RULES_BUTTON = (By.XPATH, '//*[@id="save"]') #确认保存循环赛设置按钮

    LIST_ROUND_MATCH = [ROUND_1_MATCH_BUTTON, ROUND_2_MATCH_BUTTON, ROUND_3_MATCH_BUTTON, ROUND_4_MATCH_BUTTON] #匹配方式集合
    LIST_MATCH_RANDOM = [ROUND_1_MATCH_RANDOM_BUTTON, ROUND_2_MATCH_RANDOM_BUTTON, ROUND_3_MATCH_RANDOM_BUTTON, ROUND_4_MATCH_RANDOM_BUTTON] #随机匹配方式集合
    LIST_MATCH_POWER = [ROUND_1_MATCH_POWER_BUTTON, ROUND_2_MATCH_POWER_BUTTON, ROUND_3_MATCH_POWER_BUTTON, ROUND_4_MATCH_POWER_BUTTON] #实力匹配方式集合
    LIST_SINGLE = [ROUND_1_SINGLE_BUTTON, ROUND_2_SINGLE_BUTTON, ROUND_3_SINGLE_BUTTON, ROUND_4_SINGLE_BUTTON] #SINGLE FILFHT集合
    LIST_DOUBLE = [ROUND_1_DOUBLE_BUTTON, ROUND_2_DOUBLE_BUTTON, ROUND_3_DOUBLE_BUTTON, ROUND_4_DOUBLE_BUTTON] #DOUBLE FLIGHT集合
    LIST_TRIPLE = [ROUND_1_TRIPLE_BUTTON, ROUND_2_TRIPLE_BUTTON, ROUND_3_TRIPLE_BUTTON, ROUND_4_TRIPLE_BUTTON] #TRIPE FLIGHT集合

    #------------------------------辩论赛事，淘汰赛规则设置----------------------------------
    DEBATE_OUT_EVENT_SETTING_BUTTON = (By.XPATH, '/html/body/div[3]/div[2]/div[1]/a[2]') #淘汰赛规则设置按钮
    DEBATE_WIN_NUMBER = (By.XPATH, '//*[@id="knock"]/div/div[1]/input') #晋级队伍输入框
    DEBATE_CONFIRM_BUTTON = (By.XPATH, '//*[@id="knock"]/div/div[1]/a') #保存按钮

    PARTIAL_JUDGMENT = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[1]/div[1]/input') #裁判输入框
    PARTIAL_SINGLE_BUTTON = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[1]/div[2]/label') #SINGLE FLIGHT
    PARTIAL_DOUBLE_BUTTON = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[1]/div[3]/label') #DOUBLE FLIGHT
    PARTIAL_TRIPLE_BUTTON = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[1]/div[4]/label') #TRIPLE FLIGHT

    QUARTERFINALS_JUDGMENT = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[2]/div[1]/input') #裁判输入框
    QUARTERFINALS_SINGLE_BUTTON = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[2]/div[2]/label') #SINGLE FLIGHT
    QUARTERFINALS_DOUBLE_BUTTON = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[2]/div[3]/label') #DOUBLE FLIGHT
    QUARTERFINALS_TRIPLE_BUTTON = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[2]/div[4]/label') #TRIPLE FLIGHT

    SEMIFINALS_JUDGMENT = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[3]/div[1]/input') #裁判输入框
    SEMIFINALS_SINGLE_BUTTON = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[3]/div[2]/label') #SINGLE FLIGHT
    SEMIFINALS_DOUBLE_BUTTON = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[3]/div[3]/label') #DOUBLE FLIGHT
    SEMIFINALS_TRIPLE_BUTTON = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[3]/div[4]/label') #TRIPLE FLIGHT

    FINALS_JUDGMENT = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[4]/div[1]/input') #裁判输入框
    FINALS_SINGLE_BUTTON = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[4]/div[2]/label') #SINGLE FLIGHT
    FINALS_DOUBLE_BUTTON = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[4]/div[3]/label') #DOUBLE FLIGHT
    FINALS_TRIPLE_BUTTON = (By.XPATH, '//*[@id="knock"]/div/div[2]/ul/li[4]/div[4]/label') #TRIPLE FLIGHT

    SAVE_BUTTON = (By.XPATH, '//*[@id="save"]') #点击保存按钮


