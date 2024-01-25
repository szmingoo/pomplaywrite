# coding=utf-8
from playwright.sync_api import expect
from pages.new_task_page import NewTaskPage
import allure
import pytest
from playwright.sync_api import sync_playwright
from com import args
import re


@allure.feature("新建任务页面")
class TestNewTaskPage:
    def setup_class(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)  # 有头模式运行headless=False
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        args.login(self.page,"zgy","123456")
        self.new_task = NewTaskPage(self.page)
        self.new_task.click_new_task_btn()

    @pytest.mark.s
    @allure.title("用例标题：任务名称输入校验")
    @allure.description('操作步骤：输入中文')
    def test_input_task_name(self):
        self.new_task.fill_task_name(args.get_time())

    @allure.title("用例标题：上传卷宗")
    @allure.description('操作步骤：点击上传按钮，上传本地文件')
    def test_upload(self):
        self.new_task.click_upload_btn(args.get_dir_file("data","（2021）青2822执276号.zip")[1])

    @allure.title("用例标题：创建任务")
    @allure.description('操作步骤：点击创建任务按钮')
    def test_create_task(self):
        while True:
            state = self.new_task.get_upload_state_text()
            if state=="完成":
                break
            self.page.wait_for_timeout(10)
        self.new_task.click_create_task_btn()
        expect(self.page).to_have_url(re.compile(".*home"))