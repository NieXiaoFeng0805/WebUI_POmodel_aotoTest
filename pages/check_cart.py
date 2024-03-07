# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/6 21:01
# software: PyCharm
"""
文件说明：查看购物车页面

"""
import time

from selenium.webdriver.common.by import By
from pages.Base import Base
from pages.add_cart import AddCart


class CheckCart(Base):
    def check_cart(self):
        # print(self.find(By.LINK_TEXT, "登录"))
        # exist_el = self.base_ele_isexit(self.find(By.LINK_TEXT, "登录"))
        # try:
        #     assert True, self.base_ele_isexit(self.find(By.LINK_TEXT, "登录"))
        # except:
        #     print("未找到元素")
        # else:
        #     # 悬停显示无物品
        #     try:
        #         assert '0', self.text(By.ID, 'cart_quantity')
        #     except:
        #         print("出现异常——数字不为0，显示购物车中有内容")
        #
        #     try:
        #         assert '亲，购物车中没有商品哟~', self.base_ele_isexit(self.find(By.XPATH, '/div/span/text()'))
        #     except:
        #         print("出现异常——悬停不显示预期提示")
        if self.check_hasThings():  # 有商品,跳转到购物车页面
            print("跳转到购物车页面")
            self.click(By.XPATH, '//*[@id="hd-my-cart"]/a/div/span')
        else:
            # 查看鼠标悬停事件
            try:
                print("查看鼠标悬停事件")
                assert '亲，购物车中没有商品哟~', self.base_ele_isexit(self.find(By.XPATH, '/div/span/text()'))
            except:
                print("出现异常——悬停不显示预期提示")
            else:
                print("悬停事件无异常")

    def to_addThingsAndBackIndex(self, key):
        self.send_keys(By.ID, 'q', key)
        self.click(By.CLASS_NAME, 'ecsc-search-button')
        self.click(By.LINK_TEXT, '加入购物车')
        time.sleep(3)
        try:
            # 查看添加弹窗
            assert True, self.isElementExist(self.find(By.XPATH, '//*[@id="layui-layer-iframe1"]'))
        except:
            print("添加失败")
        else:
            print("添加成功，继续购物")
        time.sleep(3)
        self.frame('layui-layer-iframe1')
        self.click(By.LINK_TEXT, '继续购物')

    def check_hasThings(self):  # 判断购物车是否有商品
        # try:
        #     print(self.text(By.ID, 'cart_quantity'))
        #     assert '0', str(self.text(By.ID, 'cart_quantity'))
        # except:
        #     print("购物车内有商品")
        #     return True
        # else:
        #     print("购物车内无商品")
        #     return False
        print(self.text(By.ID, 'cart_quantity'))
        if self.text(By.ID, 'cart_quantity') == 0:
            print("购物车内无商品")
            return False
        else:
            print("购物车内有商品")
            return True
