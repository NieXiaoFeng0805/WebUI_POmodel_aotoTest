# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/2/18 19:45
# software: PyCharm
"""
文件说明：登录页面

"""

from pages.Base import Base
from selenium.webdriver.common.by import By


class Login(Base):
    def login(self, phone, pwd, ver):
        self.click(By.LINK_TEXT, '登录')
        self.send_keys(By.ID, 'username', phone)
        self.send_keys(By.ID, 'password', pwd)
        self.send_keys(By.ID, 'verify_code', ver)
        self.click(By.NAME, 'sbtbutton')

    def if_login_success(self):
        return self.base_ele_isexit(self.find(By.LINK_TEXT, "安全退出"))

    def safe_quit(self):
        self.click(By.LINK_TEXT,"安全退出")