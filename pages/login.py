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
        self.send_keys(By.XPATH, '//*[@id="username"]', phone)
        self.send_keys(By.XPATH, '//*[@id="password"]', pwd)
        self.send_keys(By.XPATH, '//*[@id="verify_code"]', ver)
        self.click(By.XPATH, '//*[@id="loginform"]/div/div[6]/a')

    def if_login_success(self):
        return self.base_ele_isexit(By.LINK_TEXT, "安全退出")

    def safe_exit(self):
        return self.click(By.LINK_TEXT, "安全退出")