# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/2 16:36
# software: PyCharm
"""
文件说明：用户界面

"""
from pages.Base import Base
from selenium.webdriver.common.by import By
from pages.index import Index


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

    def check_user_info(self):
        """
        查看个人信息
        :return:
        """
        pass

    def check_address(self):
        """
        查看收货地址
        :return:
        """
        pass

    def to_message(self):
        '''
        查看消息
        :return:
        '''
        pass

    def to_point_store(self):
        '''
        进入积分商城
        :return:
        '''
        pass

    def to_my_cart(self):
        '''
        进入我的购物车
        :return:
        '''
        pass

    def to_my_account(self):
        '''
        查看账户余额
        :return:
        '''

    def to_check_coupon(self):
        '''
        优惠卷
        :return:
        '''

    def to_check_point(self):
        '''
        查看积分
        :return:
        '''

    def to_vip(self):
        '''
        查看vip
        :return:
        '''
