# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/26 17:25
# software: PyCharm
"""
文件说明：vip界面

"""
from pages.Base import Base
from selenium.webdriver.common.by import By


class Vip(Base):
    def check_vip(self):
        try:
            self.click(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[1]/div[3]/ul[2]/li[2]/a/span')

        except:
            print("查看用户VIP失败")
        else:
            print("查看用户VIP")
