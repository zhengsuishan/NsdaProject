# -*- coding:utf-8 -*-
# 登录测试用例
import unittest
from NSDAEvent.pages.login_page import LoginPage
from NSDAEvent.cases.init_driver import InitDriver

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = InitDriver.get_driver(InitDriver)
        cls.title = '选手报名管理 - NSDA'

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.get_data()
        res = login_page.login()
        self.assertEqual(res, self.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()