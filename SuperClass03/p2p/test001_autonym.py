# 此脚本提供实名认证的测试
import unittest,os
from selenium import webdriver
from p2p_common import set_flash
from time import sleep
from base import get_ip_info

class TestAutoNYM(unittest.TestCase):
    
    def setUp(self):
        # 第一步：初始化相关的参数
        self.driver = webdriver.Chrome()
        self.base_url = get_ip_info()+"/"
        print(self.base_url)
        # 设置元素识别超时时间
        self.driver.implicitly_wait(20)
        # 设置页面加载超时时间
        self.driver.set_page_load_timeout(20)
        # 设置异步脚本加载超时时间
        self.driver.set_script_timeout(20)
        # 最大化浏览器窗口
        self.driver.maximize_window()
        # 得到项目的地址
        self.path = os.path.dirname(os.getcwd())
        print(self.path)
        # 进行flash的设置
#         set_flash(self.driver,self.base_url,self.path)
    
    def test_01(self):
        # 第二步：打开被测网站
        driver = self.driver
        driver.get(self.base_url)
        # 第三步：执行测试动作
        sleep(3)

    
    def tearDown(self):
        self.driver.quit()
        
        
        