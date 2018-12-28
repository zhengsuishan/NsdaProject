# -*- coding:utf-8 -*-
# 比赛教室定位器
from selenium.webdriver.common.by import By

class RoomLocator(object):

    ROOM_BUTTON = (By.XPATH, '/html/body/div[3]/div[1]/div/div[4]/a/p') #比赛教室管理
    ADD_ROOM = (By.XPATH, '//*[@id="addroom"]') #添加比赛教室
    ADD_ROOM_FRAME = (By.XPATH, 'fg-layer-iframe1') #弹出框frame
    ROOM_NAME = (By.XPATH, '//*[@id="roomname"]') #教室名称输入框
    CONFIRM_BUTTON = (By.XPATH, '//*[@id="save"]') #确认添加

    #------------------------教室名称--------------------------
    ROOM_NAME_LIST = ['101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '112', '112', '113', '114', '115'] #教室名称