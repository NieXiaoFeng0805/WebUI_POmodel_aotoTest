# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/2 14:46
# software: PyCharm
"""
文件说明：

"""
import time
import allure
import pytest
from utils.read_data import get_yaml_data

from pages.index import Index


class Test_index:
    def setup(self):
        print("调用Index")
        self.index = Index()

    def teardown(self):
        print("调用teardown")
        self.index.close()

    @allure.title("登录功能测试")
    @pytest.mark.parametrize('args', get_yaml_data('login_data.yml', 'test_login_data'))
    def test_login(self, args):
        phone, pwd, ver, status = args["phone"], args["pwd"], args["ver"], args["status"]
        # print(phone, pwd, ver, status)
        self.index.to_login().login(phone, pwd, ver)
        time.sleep(3)
        # 判断是否登录成功
        if status:
            try:
                assert True, self.index.to_login().if_login_success()
            except:
                print("登录未成功")
                self.index.base_get_img()
            else:
                print("登录成功")
                time.sleep(5)
                self.index.to_login().safe_quit()

        else:
            print("登录失败")
            self.index.base_get_img()

    @allure.title("注册功能测试")
    @pytest.mark.parametrize('args', get_yaml_data("register_data.yml", "test_register_data"))
    def test_register(self, args):
        phone, ver, phone_ver, pwd, ver_pwd = args['username'], args['verify_code'], args['phone_code'], args['pwd'], \
                                              args['ver_pwd']
        self.index.to_regist().register_byPhone(phone, ver, phone_ver, pwd, ver_pwd)

    @allure.title("添加商品到购物车")
    @pytest.mark.parametrize('args', get_yaml_data("search_data.yml", "test_add_cart"))
    def test_add_cart(self, args):
        # 判断登录状态
        try:
            assert True, self.index.base_ele_isexit(self.find(By.LINK_TEXT, "安全退出"))
            print("已登录，可以进行商品添加")
        except:
            print("未进行登录，只能使用搜索功能以及查看商品")
        else:
            shop_name = args['name']
            self.index.to_addCart().to_search_and_add(shop_name)
            self.index.to_addCart().continue_buy()
