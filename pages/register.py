# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/3 14:33
# software: PyCharm
"""
文件说明：注册界面

"""
import time

from pages.Base import Base
from selenium.webdriver.common.by import By


class Register(Base):
    def register_byPhone(self, phone, ver, phone_ver, pwd, ver_pwd):
        self.click(By.LINK_TEXT, '注册')
        self.click(By.LINK_TEXT, '手机注册')
        self.send_keys(By.ID, 'username', phone)  # 用户名
        self.send_keys(By.NAME, 'verify_code', ver)  # 验证码
        self.click(By.ID, 'count_down')  # 店家发送短信验证码
        time.sleep(5)  # 发送短信等待5s
        self.send_keys(By.ID, 'code', phone_ver)  # 填写短信验证码
        self.send_keys(By.ID, 'password', pwd)  # 输入密码
        self.send_keys(By.ID, 'password2', ver_pwd)  # 确认密码
        self.click(By.LINK_TEXT, '同意协议并注册')

    def register_byMail(self, mail, ver, mail_ver, pwd, ver_pwd):
        self.click(By.LINK_TEXT, '邮箱注册')
