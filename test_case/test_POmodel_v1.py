# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/2/28 19:55
# software: PyCharm
"""
文件说明：

"""
import time

import allure
import pytest
import yaml
from utils.read_data import get_yaml_data
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.Index import Index


class Test_POmodel_v1:

    # def setup_class(self):
    #     print("setup_class：整个测试类开始前只执行一次")
    #
    # def teardown_class(self):
    #     print("teardown_class：整个测试类结束后只执行一次")
    #
    # def setup_method(self):
    #     print("setup_method：类里面每个用例执行前都会执行")
    #
    # def teardown_method(self):
    #     print("teardown_method：类里面每个用例结束后都会执行")

    def setup(self):
        print("setup：类里面每个用例执行前都会执行")
        self.index = Index()

    def teardown(self):
        print("teardown：类里面每个用例结束后都会执行")
        self.index.close()

    @allure.title("登录测试")
    @pytest.mark.parametrize("args", get_yaml_data('login_data.yml', 'test_login_data'))
    def test_login(self, args):
        phone, pwd, ver, status = args["phone"], args["pwd"], args["ver"], args["status"]
        print(phone,pwd,ver,status)
        self.index.to_login().login(phone, pwd, ver)
        if status == 'True':
            try:
                assert self.index.to_login().if_login_success(), True
                print(" 登录成功，进行安全退出")
                self.index.to_login().safe_exit()
            except:
                self.index.base_get_img()
                time.sleep(5)
        else:
            self.index.base_get_img()
