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
# from pages.add_cart import Add_Cart


class Index(Base):
    def to_login(self):
        return Login(self.driver)

    def to_regist(self):
        self.click(By.LINK_TEXT, '注册')
        return

    def to_search(self):
        self.send_keys(By.XPATH, '//*[@id="q"]', '手机')
        self.click(By.XPATH, '//*[@id="searchForm"]/button')
        # self.window(self.driver.window_handles[-1])
        return Search(self.driver)

    def to_addCart(self):
        return Add_Cart(self.driver)
