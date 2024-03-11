# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/11 16:42
# software: PyCharm
"""
文件说明：
帮助中心
"""
import time

from selenium.webdriver.common.by import By
from pages.Base import Base


class HelpCenter(Base):
    def check_help_center(self):
        # 判断是否登录
        if self.skip_login():
            # 点击帮助中心
            try:
                assert True, self.base_ele_isexit(self.find(By.XPATH, '/html/body/div[1]/div/a[1]/img'))
            except:
                print("跳转失败")
            else:
                self.click(By.LINK_TEXT, '帮助中心')
                print("进入帮助中心")
                time.sleep(5)
        else:
            print("未登录，无法查看")
