# -*- coding:utf-8 -*-
# 添加裁判测试用例
import unittest
from NSDAEvent.pages.judge_add_page import JudgeAddPage

class Judge(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.judge_page = JudgeAddPage()

    def test_add_judge(self):
        self.judge_page.get_data()
        self.judge_page.add_judge()

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()