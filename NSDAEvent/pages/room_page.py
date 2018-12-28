# -*- coding:utf-8 -*-
# 添加教室UI操作
from NSDAEvent.locators.room_locator import RoomLocator
from NSDAEvent.pages.init_driver import InitDriver
from NSDAEvent.settings.data import Data
import time

class RoomPage(object):

    driver = None
    wait_time = None

    def get_data(self):
        self.driver = InitDriver.get_driver(InitDriver)
        self.wait_time = Data.wait_time
        self.room_number = RoomLocator.ROOM_NAME_LIST.__len__()

    def add_room(self):
        self.driver.find_element(RoomLocator.ROOM_BUTTON[0], RoomLocator.ROOM_BUTTON[1]).click()
        time.sleep(1.0)

        for i in range(0, self.room_number):
            self.driver.find_element(RoomLocator.ADD_ROOM[0], RoomLocator.ADD_ROOM[1]).click()
            time.sleep(1.0)
            self.driver.switch_to.frame(RoomLocator.ADD_ROOM_FRAME)
            time.sleep(1.0)
            self.driver.find_element(RoomLocator.ROOM_NAME[0], RoomLocator.ROOM_NAME[1]).send_keys(RoomLocator.ROOM_NAME_LIST[i])
            time.sleep(0.5)
            self.driver.find_element(RoomLocator.CONFIRM_BUTTON[0], RoomLocator.CONFIRM_BUTTON[1]).click()
            time.sleep(1.0)