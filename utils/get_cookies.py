# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/2/19 11:41
# software: PyCharm
"""
文件说明：先成功登录再获取登录状态，获得cookie后即可跳过登录

"""
from selenium import webdriver
import time
import json
import os

page_url = 'http://localhost/index.php'
save_cookies_path = './login_cookies.json'


def get_login_cookies(page_url, save_cookies_path):
    driver = webdriver.Chrome()
    driver.get(url=page_url)
    time.sleep(20)

    if not os.path.exists(save_cookies_path):
        open(save_cookies_path, 'w').close()

    with open(save_cookies_path, 'w') as f:
        # 保存为json格式
        f.write(json.dumps(driver.get_cookies()))
    driver.close()


get_login_cookies(page_url, save_cookies_path)
