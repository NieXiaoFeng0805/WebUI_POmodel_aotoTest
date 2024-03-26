# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/2/18 19:46
# software: PyCharm
"""
文件说明：

"""
import unittest
import time
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.Index import Index
from ddt import ddt, data, unpack, file_data


@ddt
class Test_v1(unittest.TestCase):
    def setUp(self) -> None:
        self.index = Index()

    def tearDown(self) -> None:
        self.index.close()

    @file_data('../data/login_data.yml')
    def test_login(self, phone, pwd, ver, status):
        self.index.to_login().login(phone, pwd, ver)
        if status == 'True':
            try:
                assert self.index.to_login().if_login_success(), True
            except:
                self.index.base_get_img()
                time.sleep(8)
            print(" 登录成功，进行安全退出")
            self.index.to_login().safe_exit()
        else:
            self.index.base_get_img()
