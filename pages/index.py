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


class Index(Base):
    def to_login(self):
        return Login(self.driver)

    def to_regist(self):
        return Register(self.driver)

    def to_search(self):
        return Search(self.driver)

    def to_addCart(self):
        return AddCart(self.driver)
