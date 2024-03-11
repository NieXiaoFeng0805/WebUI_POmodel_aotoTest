# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/10 20:00
# software: PyCharm
"""
文件说明：
我的订单页面
"""
import time

from selenium.webdriver.common.by import By
from pages.Base import Base


class MyCart(Base):
    def check_MyCart(self):
        # 已登录
        if self.judge_login():
            time.sleep(2)
            # 点击我的购物车
            self.click(By.XPATH, '//*[@id="hd-my-cart"]/a/div/span')
            # 购物车内是否有物品
            try:
                assert True, self.base_ele_isexit(self.find(By.LINK_TEXT, '去结算'))
            except:
                print("购物车内无商品")
            else:
                shop_num = self.text(By.XPATH, '//*[@id="tpshop-cart"]/div[1]/ul/li/a/em')
                print("购物车内有{}件商品".format(shop_num))

    def judge_login(self):
        try:
            # 登录cookie
            self.driver = self.skip_login()
            assert True, self.driver.base_ele_isexit(self.driver.find(By.LINK_TEXT, '安全退出'))
        except:
            print("未完成登录，完成登录后可查看！")
            return False
        else:  # 已登录
            print("正在显示您的购物车")
            return True
