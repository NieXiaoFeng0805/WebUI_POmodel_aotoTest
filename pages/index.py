# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/2/18 19:45
# software: PyCharm
"""
文件说明：首页

"""
from pages.Base import Base
from selenium.webdriver.common.by import By

# from pages.search_page import Search
from pages.login import Login
from pages.add_cart import AddCart
from pages.register import Register
from pages.check_cart import CheckCart
from pages.my_cart import MyCart
from pages.my_order import MyOrder
from pages.my_history import MyHistory
from pages.my_collections import MyCollections
from pages.help_center import HelpCenter


class Index(Base):
    def to_login(self):  # 跳转登录
        return Login(self.driver)

    def to_regist(self):  # 跳转注册
        return Register(self.driver)

    def to_search(self):  # 搜索商品
        return Search(self.driver)

    def to_addCart(self):  # 加入购物车
        return AddCart(self.driver)

    def to_check_cart(self):  # 查看购物车
        return CheckCart(self.driver)

    def to_check_MyCart(self):  # 查看登录后的购物车
        return MyCart(self.driver)

    def to_check_MyOrder(self):  # 查看我的订单
        return MyOrder(self.driver)

    def to_check_MyHistory(self):  # 查看浏览记录
        return MyHistory(self.driver)

    def to_check_MyCollections(self):  # 查看收藏
        return MyCollections(self.driver)

    def to_HelpCenter(self):  # 进入帮助中心
        return HelpCenter(self.driver)
