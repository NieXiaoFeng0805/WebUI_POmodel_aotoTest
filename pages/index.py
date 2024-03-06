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
