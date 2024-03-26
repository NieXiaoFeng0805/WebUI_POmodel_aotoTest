# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/26 16:56
# software: PyCharm
"""
文件说明：
用户信息界面
"""
from pages.Base import Base
from selenium.webdriver.common.by import By


class MyMessage(Base):
    def check_my_message(self):
        self.click(By.LINK_TEXT, '消息')
