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
    def back_home_1(self):
        '''
        回到首页
        :return:
        '''
        if self.skip_login():
            self.click(By.LINK_TEXT, 'summer')  # 进入
            self.click(By.LINK_TEXT, '返回商城首页')

    def back_home_2(self):
        '''
        回到首页
        :return:
        '''
        if self.skip_login():
            self.click(By.LINK_TEXT, 'summer')  # 进入
            self.click(By.LINK_TEXT, '首页')

    def safe_quit(self):
        '''
        安全退出
        :return:
        '''
        if self.skip_login():
            self.click(By.LINK_TEXT, '安全退出')

    def to_user_info(self):
        """
        查看个人信息
        :return:
        """
        return UserInfo(self.driver)

    def to_user_address(self):
        """
        查看收货地址
        :return:
        """
        return UserInfo(self.driver)

    def to_message(self):
        '''
        查看消息
        :return:
        '''
        return MyMessage(self.driver)

    def to_point_store(self):
        '''
        进入积分商城
        :return:
        '''
        return PointStore(self.driver)

    def to_my_cart(self):
        '''
        进入我的购物车
        :return:
        '''
        return CheckCart(self.driver)

    def to_my_account(self):
        '''
        查看账户余额
        :return:
        '''
        return UserAccount(self.driver)

    def to_check_coupon(self):
        '''
        优惠卷
        :return:
        '''
        return UserCoupon(self.driver)

    def to_check_point(self):
        '''
        查看积分
        :return:
        '''
        return UserPoint(self.driver)

    def to_vip(self):
        '''
        查看vip
        :return:
        '''
        return Vip(self.driver)
