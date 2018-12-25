from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import unittest,pytest,time
from comm.LoginPage import LoginPage
from comm.BasePage import BasePage
class Test_Think_sns(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.bg=BasePage(self.driver)
        try:
            self.lp=LoginPage(self.driver,"https://yun.baidu.com")
        except Exception as e:
            print("超时，截取当前图片")
            self.bg.save_screen("打开网页超时_")
            raise e            
    def test_login(self):
        self.lp.loging("13550848524","13550848524")

            
        
        
