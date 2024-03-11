# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/10 21:48
# software: PyCharm
"""
文件说明：

"""
from selenium import webdriver
import time
import json

# 填写webdriver的保存目录
driver = webdriver.Chrome()

# 记得写完整的url 包括http和https
driver.get('http://localhost/index.php')

# 程序打开网页后20秒内手动登陆账户
time.sleep(20)

with open('cookies_test.json', 'w') as cookief:
    # 将cookies保存为json格式
    cookief.write(json.dumps(driver.get_cookies()))

driver.close()

# 填写webdriver的保存目录
driver = webdriver.Chrome()

# 记得写完整的url 包括http和https
driver.get('http://localhost/index.php')
# 首先清除由于浏览器打开已有的cookies
driver.delete_all_cookies()

with open('cookies_test.json', 'r') as cookief:
    # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookieslist = json.load(cookief)
    for cookie in cookieslist:
        driver.add_cookie(cookie)
time.sleep(5)
driver.refresh()
driver.close()
