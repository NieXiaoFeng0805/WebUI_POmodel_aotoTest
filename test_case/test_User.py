# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/25 19:32
# software: PyCharm
"""
文件说明：测试用户中心

"""
import time
import allure
import pytest
from utils.read_data import get_yaml_data
from pages.User import User


class Test_User:
    def setup(self):
        print("调用User")
        self.user = User()

    def teardown(self):
        print("调用teardown")
        self.user.close()

    def test_back_home(self):
        for i in range(2):
            if i == 0:
                self.user.back_home_1()  # 方式一返回
            else:
                self.user.back_home_2()  # 方式二返回

    def test_safe_quit(self):
        self.user.safe_quit()

    def test_user_message(self):
        self.user.check_user_info()

    def test_user_address(self):
        self.user.check_address()

    def test_message(self):
        self.user.to_message()

    def test_point_store(self):
        self.user.to_point_store()

    def test_my_cart(self):
        self.user.to_my_cart()

    def test_my_account(self):
        self.user.to_my_account()

    def test_coupon(self):
        self.user.to_check_coupon()

    def test_user_point(self):
        self.user.to_check_point()

    def test_vip(self):
        self.user.to_vip()
