# coding=utf-8
import pytest
import os

if __name__ == '__main__':
    pytest.main(["-n 2","--dist=loadfile","-sq","--alluredir", 'results'])#分布式运行根据文件名来分组
    os.system("allure generate -c results -o report --clean-alluredir")
    os.system('allure open D:/code/pwpomdcs/report')

# playwright codegen

# 阿里云: -i http://mirrors.aliyun.com/pypi/simple/
# 豆瓣: -i http://pypi.douban.com/simple/
# 清华: -i https://pypi.tuna.tsinghua.edu.cn/simple
# 中国科技大学: -i https://pypi.mirrors.ustc.edu.cn/simple/
# 华中理工大学: -i http://pypi.hustunique.com/