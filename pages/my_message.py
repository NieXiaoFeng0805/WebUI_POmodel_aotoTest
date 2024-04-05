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
        try:
            self.click(By.XPATH, '/html/body/div[2]/div/div[3]/ul/li[3]/a')
        except:
            print("进入消息界面失败")
        else:
            print("进入消息界面成功")
