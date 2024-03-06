# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/6 21:01
# software: PyCharm
"""
文件说明：查看购物车页面

"""
import time

from pages.Base import Base
from selenium.webdriver.common.by import By


class CheckCart(Base):
    def check_cart(self):
        # 未登录状态下的查看购物车
        time.sleep(2)
        # print(self.find(By.LINK_TEXT, "登录"))
        # exist_el = self.base_ele_isexit(self.find(By.LINK_TEXT, "登录"))
        try:
            assert True, self.base_ele_isexit(self.find(By.LINK_TEXT, "登录"))
        except:
            print("未找到元素")
        else:
            # 悬停显示无物品
            try:
                assert '0', self.text(By.ID, 'cart_quantity')
            except:
                print("出现异常——数字不为0，显示购物车中有内容")

            try:
                assert '亲，购物车中没有商品哟~', self.base_ele_isexit(self.find(By.XPATH, '/div/span/text()'))
            except:
                print("出现异常——悬停不显示预期提示")


