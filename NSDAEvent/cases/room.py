# -*- coding:utf-8 -*-
# 添加教室测试用例
import unittest
from NSDAEvent.pages.room_page import RoomPage

class Room(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.room_page = RoomPage()

    def test_add_room(self):
        self.room_page.get_data()
        self.room_page.add_room()

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()