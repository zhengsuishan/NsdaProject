# -*- coding:utf-8 -*-
# 设置规则测试用例
import unittest
from NSDAEvent.pages.setting_rules_page import SettingRulesPage


class Rules(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.setting_rule_page = SettingRulesPage()
        cls.setting_rule_page.get_data()

    def test_1_set_point(self):
        self.setting_rule_page.set_points()


    @classmethod
    def tearDownClass(cls):
        pass
        #cls.driver.close()

if __name__ == '__main__':
    unittest.main()