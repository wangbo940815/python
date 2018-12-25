from comm.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
class LoginPage:
    get_in_login="//*[@id='TANGRAM__PSP_4__footerULoginBtn']"
    username_xpath= "//*[@id='TANGRAM__PSP_4__userName']"
    password_xpath="//*[@id='TANGRAM__PSP_4__password']"
    login_click="//*[@id='TANGRAM__PSP_4__submit']"
    def __init__(self,driver,url):
        self.driver=driver
        self.driver.get(url)
#         self.bg_t=BasePage(self.driver)
    def loging(self,username,password):
        self.bg_t=BasePage(self.driver)
        self.bg_t.get_element(self.get_in_login).click()
        self.bg_t.get_element(self.username_xpath).send_keys(username)
        self.bg_t.get_element(self.password_xpath).send_keys(password)
        """点击登录"""
        self.bg_t.get_element(self.login_click).click()
    
        
        