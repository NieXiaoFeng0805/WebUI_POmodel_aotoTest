# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/26 17:23
# software: PyCharm
"""
文件说明：用户积分界面

"""
from pages.Base import Base
from selenium.webdriver.common.by import By


class UserPoint(Base):
    def check_user_point(self):
        self.click(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[1]/div[3]/ul[1]/li[3]/a/span')
