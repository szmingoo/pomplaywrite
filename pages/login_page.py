# coding=utf-8
from com.ini_opt import ReadConfig as rc

class LoginPage:
    def __init__(self,page):
        self.host=rc().get_host_url()
        self.page=page
        self.username_input=self.page.get_by_placeholder("请输入登录名")
        self.password_input=self.page.get_by_placeholder("请输入密码")
        self.login_btn=self.page.get_by_role("button", name="登 录")

    def navigate(self):
        self.page.goto(self.host+"/dist/index.html#/login")

    def fill_username(self,username):
        self.username_input.fill(username)

    def fill_password(self,password):
        self.password_input.fill(password)

    def click_login_btn(self):
        self.login_btn.click()