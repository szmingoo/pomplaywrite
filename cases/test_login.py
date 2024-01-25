# coding=utf-8
from playwright.sync_api import expect
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright
import allure
import pytest
from com import args
import re

@allure.feature("登录页面")
class TestLogin:#以Test开头
    def setup_class(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)  # 有头模式运行
        self.context = self.browser.new_context()
        self.page = self.context.new_page()


    @pytest.mark.run(order=1)#如果类里面只有一个方法，那不能用该装饰器排序
    @allure.title("用例标题：登录失败")
    @allure.description('操作步骤：输入错误的密码')
    def test_input_error_password(self):#以test开头
        args.login(self.page, "zgy", "abcdef")
        expect(self.page).to_have_url(re.compile(".*login"))
        self.page.wait_for_timeout(8000)

    @pytest.mark.run(order=2)
    @allure.title("用例标题：登录成功")
    @allure.description('操作步骤：输入正确的用户名和密码')
    def test_success(self):
        args.login(self.page, "zgy", "123456")
        expect(self.page).to_have_url(re.compile(".*home"))
        self.page.wait_for_timeout(8000)


    # @pytest.mark.skipif(reason='本次不执行')
    # @allure.title("用例标题：跳过")
    # def test_input_error(self):pass

