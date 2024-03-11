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
        shop_name = args['name']
        self.index.to_addCart().to_search_and_add(shop_name)
        self.index.to_addCart().continue_buy()

    @allure.title("查看无商品的购物车")
    def test_check_cart_ByNoThings(self):
        self.index.to_check_cart().check_cart()

    @allure.title("查看有商品的购物车")
    @pytest.mark.parametrize('args', get_yaml_data("search_data.yml", "test_add_cart"))
    def test_check_cart_ByHasThings(self, args):
        shop_name = args['name']
        self.index.to_check_cart().to_addThingsAndBackIndex(shop_name)
        self.index.to_check_cart().check_cart()

    @allure.title("查看登录后的购物车")
    def test_check_MyCart(self):
        self.index.to_check_MyCart().check_MyCart()

    @allure.title("查看我的订单")
    def test_check_MyOrder(self):
        self.index.to_check_MyOrder().check_myOrder()

    @allure.title("查看浏览记录")
    def test_check_MyHistory(self):
        self.index.to_check_MyHistory().check_my_history()

    @allure.title("查看我的收藏")
    def test_check_MyCollections(self):
        self.index.to_check_MyCollections().check_my_collections()

    @allure.title("进入帮助中心")
    def test_in_HelpCenter(self):
        self.index.to_HelpCenter().check_help_center()
