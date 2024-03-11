# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/11 15:51
# software: PyCharm
"""
文件说明：
浏览记录页面
"""
import time

from selenium.webdriver.common.by import By
from pages.Base import Base


class MyHistory(Base):
    def check_my_history(self):
        # 判断是否登录
        if self.skip_login():
            # 点击我的订单
            try:
                assert True, self.base_ele_isexit(self.find(By.CLASS_NAME, 'goodpiece'))
            except:
                print("跳转失败")
            else:
                self.click(By.LINK_TEXT, '我的浏览')
                print("展示我的浏览记录")
                time.sleep(5)
        else:
            print("未登录，无法查看")
