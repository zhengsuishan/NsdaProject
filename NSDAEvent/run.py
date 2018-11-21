# -*- coding:utf-8 -*-
# 组织测试用例

import unittest
from NSDAEvent.cases.login import Login

if __name__ == '__main__':
    suite = unittest.TestSuite()

    cases = [Login('test_login')]
    suite.addTests(cases)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run()