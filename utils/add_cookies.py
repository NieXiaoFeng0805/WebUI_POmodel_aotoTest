# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/10 20:13
# software: PyCharm
"""
文件说明：
将获取到的登录状态存放到driver中
"""

from selenium.webdriver.remote.webdriver import WebDriver

import time
import json
import yaml


# def add_cookies(driver):
#     try:
#         with open('E://Pycharm//LearnSelenium//WebUI_POmodel_aotoTest//data//test_config') as f:
#             cfg = yaml.safe_load(f_cfg.read())
#             # print(cfg)
#             # print(cfg['to_get_cookies'])
#     except IOError:
#         print("打开配置文件失败")
#     # 清除已有cookie
#     driver.delete_all_cookies()
#     try:
#         with open(cfg['to_get_cookies']['cookies_save_path'], r) as cookief:
#             # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
#             cookieslist = json.load(cookief)
#             for cookie in cookieslist:
#                 driver.add_cookie(cookie)
#     except IOError:
#         print("打开cookie文件失败")
#     time.sleep(5)
#     driver.refresh()
#     return driver


def add_cookies(driver: WebDriver):
    # 首先清除由于浏览器打开已有的cookies
    driver.delete_all_cookies()
    # 配置文件路径
    config_yaml = 'E://Pycharm//LearnSelenium//WebUI_POmodel_aotoTest//data//test_config'
    with open(config_yaml, 'r', encoding='utf-8') as f:
        cookie_path_list = yaml.safe_load(f.read())
    cookies_path = cookie_path_list['cookies_path']['login']
    with open(cookies_path, 'r') as cookie_f:
        # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
        cookie_list = json.load(cookie_f)
        for cookie in cookie_list:
            driver.add_cookie(cookie)
    time.sleep(5)
    driver.refresh()
    return driver
