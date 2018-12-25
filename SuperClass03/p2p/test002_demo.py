# 此脚本提供实名认证的测试
import unittest,os
from base import SeleniumDriver
from time import sleep
from base import get_ip_info,get_log_path
from base import log_decorator



class TestDemo(unittest.TestCase):
    log = get_log_path(__file__,__name__)
      
#     @log_decorator(log)
    def setUp(self,browser=None,type=None):
        # 第一步：初始化相关参数
        self.driver = SeleniumDriver(browser,type)
        self.base_url = get_ip_info()+"/"
        
    @log_decorator(log)
    def test_01(self):
        # 第二步：打开被测网站
        driver = self.driver
#         driver.get(self.base_url)
        # 第三步：执行测试动作
        self.assertEqual("xxx", "xxx")
#         driver.find_element_by_id("xxxx").click()

#     @log_decorator(log)
    def test_02(self):
        print("2222222222")
        
#     @log_decorator(log)
    def tearDown(self):
        self.driver.quit()
#         print("xxxxxxxx")

        
        