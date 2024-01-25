# coding=utf-8
from com.ini_opt import ReadConfig as rc

class NewTaskPage:
    def __init__(self,page):
        self.host = rc().get_host_url()
        self.page=page
        self.new_task_btn=self.page.get_by_text("新建评查任务")
        self.task_name_input=self.page.get_by_placeholder("请输入本次评查任务的名称")
        self.upload_btn=self.page.get_by_role("button", name="选取文件")
        self.upload_state_text = self.page.locator("//*[@id='app']/div/div[2]/div[1]/div[4]/div[2]/div[1]/div[3]")
        self.create_task_btn=self.page.get_by_role("button", name="确认创建任务")

    def navigate(self):
        self.page.goto(self.host+"/dist/index.html#/newtask")

    def get_upload_state_text(self):
        return self.upload_state_text.inner_text()

    def click_new_task_btn(self):
        self.new_task_btn.click()

    def fill_task_name(self, task_name):
        self.task_name_input.fill(task_name)

    def click_upload_btn(self,filepath):
        self.page.on("filechooser", lambda file_chooser: file_chooser.set_files(filepath))
        self.upload_btn.click()

    def click_create_task_btn(self):
        self.create_task_btn.click()