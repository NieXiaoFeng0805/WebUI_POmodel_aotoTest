# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/11 15:59
# software: PyCharm
"""
文件说明：
我的收藏
"""
import time

from selenium.webdriver.common.by import By
from pages.Base import Base

class MyCollections(Base):
    def check_my_collections(self):
        # 判断是否登录
        if self.skip_login():
            # 点击我的订单
            try:
                assert True, self.base_ele_isexit(self.find(By.CLASS_NAME, 'goodpiece'))
            except:
                print("跳转失败")
            else:
                self.click(By.LINK_TEXT, '我的收藏')
                print("展示我的收藏")
                time.sleep(5)
        else:
            print("未登录，无法查看")
