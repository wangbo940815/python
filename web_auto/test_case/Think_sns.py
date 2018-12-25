from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import unittest,time,sys
from page.LoginPage import LoginPage
from comm.BasePage import BasePage
from comm.log_decorator import  log_decorator
class Test_Think_sns(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.bg=BasePage(self.driver)
        try:
            self.lp=LoginPage(self.driver,"https://yun.baidu.com")    
        except Exception as e:
            self.bg.save_screen("打开网页超时_")
            raise e         

    @log_decorator   
    def test_login(self):
        self.lp.loging("13550848524","13550848524")

            
        
        
