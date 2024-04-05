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
from selenium.webdriver.common.by import By

page_url = 'http://localhost/index.php'
save_cookies_path = './login_cookies.json'


def get_login_cookies(page_url, save_cookies_path):
    driver = webdriver.Chrome()
    driver.get(url=page_url)

    # 程序打开网页后自动登陆账户
    driver.find_element(By.LINK_TEXT, '登录').click()
    driver.find_element(By.ID, 'username').send_keys("13800138006")
    driver.find_element(By.ID, 'password').send_keys("123456")
    driver.find_element(By.ID, 'verify_code').send_keys("8888")
    driver.find_element(By.XPATH, '//*[@id="loginform"]/div/div[6]/a').click()
    time.sleep(5)

    if not os.path.exists(save_cookies_path):
        open(save_cookies_path, 'w').close()

    with open(save_cookies_path, 'w') as f:
        # 保存为json格式
        f.write(json.dumps(driver.get_cookies()))
    driver.close()


get_login_cookies(page_url, save_cookies_path)
