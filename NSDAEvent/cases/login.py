# -*- coding:utf-8 -*-
# 登录测试用例
import unittest
from NSDAEvent.pages.login_page import LoginPage

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.title = '选手报名管理 - NSDA'
        cls.login_page = LoginPage()

    def test_login(self):
        self.login_page.get_data()
        res = self.login_page.login()
        self.assertEqual(res, self.title)

    @classmethod
    def tearDownClass(cls):
        pass
        #cls.driver.close()

if __name__ == '__main__':
    unittest.main()