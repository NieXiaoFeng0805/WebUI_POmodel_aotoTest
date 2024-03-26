# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/26 17:04
# software: PyCharm
"""
文件说明：
积分商城界面
"""
from pages.Base import Base
from selenium.webdriver.common.by import By


class PointStore(Base):
    def check_point_store(self):
        self.click(By.LINK_TEXT, '积分商城')

