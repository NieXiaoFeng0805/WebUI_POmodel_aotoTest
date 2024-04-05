# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/2 16:36
# software: PyCharm
"""
文件说明：用户界面

"""
from pages.Base import Base
from selenium.webdriver.common.by import By
from pages.Index import Index

from pages.user_info import UserInfo
from pages.my_message import MyMessage
from pages.point_store import PointStore
from pages.check_cart import CheckCart
from pages.user_account import UserAccount
from pages.user_coupon import UserCoupon
from pages.user_point import UserPoint
from pages.vip import Vip


class User(Base):

    def goto_user(self):
        # if self.skip_login():
        #     self.click(By.LINK_TEXT, 'summer')  # 进入个人界面
        # else:
        #     print("登录跳过失败")

        # 程序打开网页后自动登陆账户
        self.click(By.LINK_TEXT, '登录')
        self.send_keys(By.ID, 'username', "13800138006")
        self.send_keys(By.ID, 'password', "123456")
        self.send_keys(By.ID, 'verify_code', "8888")
        self.click(By.XPATH, '//*[@id="loginform"]/div/div[6]/a')
        self.click(By.LINK_TEXT, "summer")

    def back_home_1(self):
        '''
        回到首页
        :return:
        '''
        self.goto_user()
        try:
            self.click(By.LINK_TEXT, '返回商城首页')
        except:
            print("返回失败")
        else:
            print("返回成功")

    def back_home_2(self):
        '''
        回到首页
        :return:
        '''
        self.goto_user()
        try:
            self.click(By.LINK_TEXT, '首页')
        except:
            print("返回失败")
        else:
            print("返回成功")

    def safe_quit(self):
        '''
        安全退出
        :return:
        '''
        self.goto_user()
        try:
            self.click(By.LINK_TEXT, '安全退出')
        except:
            print("安全退出失败")
        else:
            print("退出成功")

    def to_user_info(self):
        """
        查看个人信息
        :return:
        """
        self.goto_user()
        return UserInfo(self.driver)

    def to_user_address(self):
        """
        查看收货地址
        :return:
        """
        self.goto_user()
        return UserInfo(self.driver)

    def to_message(self):
        '''
        查看消息
        :return:
        '''
        self.goto_user()
        return MyMessage(self.driver)

    def to_point_store(self):
        '''
        进入积分商城
        :return:
        '''
        self.goto_user()
        return PointStore(self.driver)

    def to_my_cart(self):
        '''
        进入我的购物车
        :return:
        '''
        self.goto_user()
        return CheckCart(self.driver)

    def to_my_account(self):
        '''
        查看账户余额
        :return:
        '''
        self.goto_user()
        return UserAccount(self.driver)

    def to_check_coupon(self):
        '''
        优惠卷
        :return:
        '''
        self.goto_user()
        return UserCoupon(self.driver)

    def to_check_point(self):
        '''
        查看积分
        :return:
        '''
        self.goto_user()
        return UserPoint(self.driver)

    def to_vip(self):
        '''
        查看vip
        :return:
        '''
        self.goto_user()
        return Vip(self.driver)
