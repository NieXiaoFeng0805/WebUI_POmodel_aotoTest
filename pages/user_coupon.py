# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/26 17:19
# software: PyCharm
"""
文件说明：用户优惠卷

"""
from pages.Base import Base
from selenium.webdriver.common.by import By


class UserCoupon(Base):
    def check_user_coupon(self):
        self.click(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[1]/div[3]/ul[2]/li[1]/a/span')
