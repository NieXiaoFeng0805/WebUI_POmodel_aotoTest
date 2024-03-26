# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/2/28 17:04
# software: PyCharm
"""
文件说明：

"""
import unittest
import csv
import time
import parameterized
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.Index import Index
from utils.read_data import get_csv_data


class Test_v2(unittest.TestCase):
    def setUp(self) -> None:
        self.index = Index()

    def tearDown(self) -> None:
        self.index.close()

    @parameterized.parameterized.expand(get_csv_data('../data/login_data.csv'))
    def test_login(self, phone, pwd, ver, status):
        self.index.to_login().login(phone, pwd, ver)  # 登录
        if status == 'True':  # 登录成功状态
            try:
                assert self.index.to_login().if_login_success(), True
            except:
                self.index.base_get_img()
                time.sleep(8)
            print(" 登录成功，进行安全退出")
            self.index.to_login().if_login_success()
        else: # 失败状态，截图
            self.index.base_get_img()
