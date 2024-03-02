# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/2 16:36
# software: PyCharm
"""
文件说明：用户姐妹界面

"""
from pages.Base import Base
from selenium.webdriver.common.by import By

class User(Base):
    def safe_quit(self):
        self.click(By.LINK_TEXT,"安全退出")
