import unittest
from base import SeleniumDriver
from base import get_ip_info
from time import sleep,time
from random import choice

class TestRegister(unittest.TestCase):

    def setUp(self,browser=None,type=None):
        # 第一步：初始化相关参数
        self.driver = SeleniumDriver(browser,type)
        self.base_url = get_ip_info()+"/"

    def test_01(self):
        # 第二步：打开被测网站
        driver = self.driver
        driver.open(self.base_url)
        # 第三步：执行测试动作
        # 定义邮箱，密码，姓名
        email = str(time()*1000)[:13]+"@qq.com"
        password = "123456"
        first_name_list = ["赵","钱","孙","李","周","吴","郑","王",
                           "冯","陈","褚","卫","蒋","沈","韩","杨"]
        second_name_list = ["艾","安","昂","敖","奥","巴","霸","白","柏",
                            "拜","班","包","保","葆","豹","鲍","暴","卑",
                            "贲","毕","闭","秘","边","鞭","彪","别","宾",
                            "邴","秉","薄","卜","布","部","才","蔡","仓",
                            "苍","操","曹","策","岑","柴","镡","昌","苌",
                            "常","昶","畅","唱","晁","巢","朝","车","陈",
                            "谌","成","承","晟","乘","程","池","迟","充","种","崇","丑","侴","初"]
        name = choice(first_name_list)+choice(second_name_list)
        # 点击 注册
        driver.find_element_by_link_text("注册").click()
        # 输入邮箱 
        driver.find_element_by_name("email").send_keys(email)
        # 输入登录密码 
        driver.find_element_by_name("passwd").send_keys(password)
        # 输入确认密码 
        driver.find_element_by_name("repasswd").send_keys(password)
        # 输入姓名 
        driver.find_element_by_name("name").send_keys(name)
        # 随机选择性别 
        sex_list = ["1","0"]
        sex = choice(sex_list)
        driver.find_element_by_xpath("//input[@name='sex' and @value='"+sex+"']").click()
        # 点击 选择地区  
        driver.find_element_by_class_name("btn_b").click()
        # 点击 四川
        driver.find_element_by_link_text("四川").click()
        # 点击 成都市
        driver.find_element_by_link_text("成都市").click()
        # 点击 确定 
        driver.find_element_by_name("input").click()
        # 选择 隐私设置 
        # 方式一：直接xpath找
        driver.find_element_by_xpath("//select[@name='baseinfoprivacy']/option[@value='0']").click()
        # 点击 立即注册 
        driver.find_element_by_name("button").click()
        sleep(2.5)
        # 点击 基本资料
        driver.find_element_by_link_text("基本资料").click() 
        sleep(0.5)
        # 第四步：判断测试结果
        # 取得姓名的value属性值，并判断   
        actual_name = driver.find_element_by_name("name").get_attribute("value")
        self.assertEqual(name, actual_name)
    
    def tearDown(self):
        # 第五步：释放资源
        self.driver.quit()

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()