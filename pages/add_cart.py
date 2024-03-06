# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/2 17:41
# software: PyCharm
"""
文件说明：

"""
import time

from pages.Base import Base
from selenium.webdriver.common.by import By


class AddCart(Base):
    def to_search_and_add(self, key):
        self.send_keys(By.ID, 'q', key)
        self.click(By.CLASS_NAME, 'ecsc-search-button')
        self.click(By.LINK_TEXT, '加入购物车')
        time.sleep(3)
        try:
            assert True, self.isElementExist(self.find(By.XPATH, '//*[@id="layui-layer-iframe1"]'))
        except:
            print("添加失败")
        else:
            print("添加成功，继续购物")

    def continue_buy(self):
        self.frame('layui-layer-iframe1')
        self.click(By.LINK_TEXT, '继续购物')
