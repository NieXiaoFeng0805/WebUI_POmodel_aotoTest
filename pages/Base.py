# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/2/17 20:29
# software: PyCharm
"""
文件说明：基类文件

"""
import os
import time
from ddt import ddt, data, unpack, file_data
import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.add_cookies import add_cookies

'''Base是所有pageobject的父类，  为子类提供公共方法， 比如初始化 driver 和退出driver
代码在base_page模块的basepage类使用——init——初始方法进行初始化操作，包括driver的复用
driver的赋值、全局的等待时间设置 == 常见隐式等待'''


class Base:
    def __init__(self, driver: WebDriver = None):
        if not driver:
            # 设置不自动关闭
            self.optioin = webdriver.ChromeOptions()
            self.optioin.add_experimental_option("detach", True)
            self.driver = webdriver.Chrome(self.optioin)
            # self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.get('http://localhost/index.php')
            # 最大化
            self.driver.maximize_window()
        else:
            self.driver = driver

    def skip_login(self):  # 跳过登录
        self.driver = add_cookies(self.driver)
        return self.driver

    def close(self):
        time.sleep(3)
        self.driver.quit()

    # 提取find方法
    def find(self, by, loc):
        return WebDriverWait(self.driver, timeout=15).until(lambda x: self.driver.find_element(by, loc))

    # 提取finds方法
    def finds(self, by, loc):
        return WebDriverWait(self.driver, timeout=15).until(lambda x: self.driver.find_elements(by, loc))

    # 提取click方法
    def click(self, by, loc):
        return self.find(by, loc).click()

    # 提取输入方法
    def send_keys(self, by, loc, v):
        return self.find(by, loc).send_keys(v)

    # 提取text
    def text(self, by, loc):
        return self.find(by, loc).text

    # 提取window
    def window(self, window_name):
        return self.driver.switch_to.window(window_name)

    # 切换frame
    def frame(self, frame_name):
        return self.driver.switch_to.frame(frame_name)

    # 截图方法
    def base_get_img(self):
        self.driver.get_screenshot_as_file('../images/{}.png'.format(time.strftime("%Y_%m_%d_%H_%M_%S")))

    # 判断元素是否存在
    def base_ele_isexit(self, loc):
        try:
            self.find(loc)
            return True
        except:
            return False

    # 选择下拉框
    def select_down(self, by, loc):
        pass

    # 定位鼠标悬停
    def mouseover(self, by, loc):
        ActionChains(self.driver).move_to_element(self.find(by, loc).perform())
