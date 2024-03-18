# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/18 13:35
# software: PyCharm
"""
文件说明：
导航栏的兑换中心界面
"""
import time

from selenium.webdriver.common.by import By
from pages.Base import Base
from selenium.webdriver.common.action_chains import ActionChains


class ExchangeCenter(Base):
    def check_exchangeCenter(self):
        # 定位下拉框
        navigator = self.find(By.CLASS_NAME, 'nav-dh')
        try:
            ActionChains(self.driver).move_to_element(navigator).perform()
        except:
            print("进入失败")
        else:
            self.click(By.LINK_TEXT, '兑换中心')
            print("进入成功")
