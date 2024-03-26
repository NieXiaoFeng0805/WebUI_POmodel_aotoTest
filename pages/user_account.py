# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/26 17:16
# software: PyCharm
"""
文件说明：
账户余额页面
"""
from pages.Base import Base
from selenium.webdriver.common.by import By


class UserAccount(Base):
    def check_account(self):
        self.click(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[1]/div[3]/ul[1]/li[2]/a/span')

