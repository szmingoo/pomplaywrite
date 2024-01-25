# coding=utf-8
from pages.login_page import LoginPage

def login(page,user,pwd):
    lp=LoginPage(page)
    lp.navigate()
    lp.fill_username(user)
    lp.fill_password(pwd)
    lp.click_login_btn()

from datetime import datetime
def get_time():
    return datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]

import os
def get_dir_file(dir_name,file_name):
    current_dir = os.path.split(os.path.realpath(__file__))[0]
    target_dir = os.path.abspath(os.path.join(current_dir, os.pardir))+'\\'+dir_name+'\\'
    target_file=target_dir+file_name
    return target_dir,target_file
