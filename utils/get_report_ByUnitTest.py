# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/2/19 11:35
# software: PyCharm
"""
文件说明：UnitTest生成测试报告

"""

from unittestreport import TestRunner
import os
from test_case.POtest_v2 import Test_v2
import BeautifulReport
import unittest

# 设置测试套件
test_unit = unittest.TestSuite()
# 套件加载并加载指定测试用例
test_unit.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_v2))
# 生成测试报告
result = BeautifulReport.BeautifulReport(test_unit)
result.report(filename="Test1", description="测试报告")
