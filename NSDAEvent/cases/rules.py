# -*- coding:utf-8 -*-
# 设置比赛规则测试用例
import unittest
from NSDAEvent.pages.setting_rules_page import SettingRulesPage
from NSDAEvent.settings.data import Data

class Rules(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.setting_rule_page = SettingRulesPage()
        cls.setting_rule_page.get_data()
        cls.success_promote = Data.SUCCESS_PTOMOTE

    def test_1_set_point(self):
        self.setting_rule_page.set_points()

    def test_2_set_round(self):
        self.setting_rule_page.set_debate_round()

    def test_3_set_out(self):
        self.setting_rule_page.set_out()

    def test_4_set_temp_day(self):
        res = self.setting_rule_page.temp_set_day()
        self.assertEqual(res, self.success_promote)

    @classmethod
    def tearDownClass(cls):
        pass
        #cls.driver.close()

if __name__ == '__main__':
    unittest.main()