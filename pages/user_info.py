# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/26 16:49
# software: PyCharm
"""
文件说明：
个人信息页面
"""
from pages.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class UserInfo(Base):
    def loc_ele(self):
        # 定位下拉框
        loc = self.find(By.CLASS_NAME, 'u-dl')
        # 悬停事件
        try:
            ActionChains(self.driver).move_to_element(loc).perform()
        except:
            return False
        else:
            return True

    def check_user_info(self):
        if self.loc_ele():
            self.click(By.LINK_TEXT, '个人信息')
            print("进入个人信息成功")

    def check_user_address(self):
        if self.loc_ele():
            self.click(By.LINK_TEXT, '收货地址')
            print("进入收货地址成功")
