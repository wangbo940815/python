import unittest
from selenium import webdriver
from time import sleep,time
from random import choice
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver

class TestRegister(unittest.TestCase):

    def setUp(self):
        # 第一步：初始化相关参数
#         self.driver = webdriver.Firefox()
        self.driver = WebDriver(command_executor='http://192.168.1.104:4444/wd/hub',
                                desired_capabilities=DesiredCapabilities.FIREFOX)
        print("初始化驱动完成~~~~~~~~~~~~~~~~")
        self.base_url = "http://172.31.31.100:8200/"
        # 设置元素识别超时时间
        self.driver.implicitly_wait(20)
        # 设置页面加载超时时间
        self.driver.set_page_load_timeout(20)
        # 设置异步脚本加载超时时间
        self.driver.set_script_timeout(20)
        print("初始化相关参数全部完成~~~~~~~~~~~~~~~~")

    def test_01(self):
        # 第二步：打开被测网站
        driver = self.driver
        driver.get(self.base_url)
        print("打开被测网站完成~~~~~~~~~~~~~~~~")
        # 第三步：执行测试动作
        # 点击 注册
        driver.find_element_by_link_text("注册").click()
        # 先定义注册时的邮箱地址、姓名、密码
        email = str(time()*1000)[:13]+"@qq.com"
        password = "123456"
        first_name_list = ["同","佟","彤","童","钭","徒","涂","屠","土","脱","完","宛","晚",
                           "万","汪","王","望","危","韦","维","蒍","隗","位","尉","温",
                           "文","闻","问","翁","瓮","邬","巫","毋","吾","吴","伍",
                           "轩","禤","旋","薛","穴","雪","寻","郇","荀","押","牙",
                           "轧","鄢","燕","延","严","言","阎","颜","晏","扬","羊",
                           "阳","杨","仰","幺","要","尧","姚","铫","药","冶","业",
                           "仵","武","务","西","析","郗","息","奚","锡","习","席"]
        second_name_list = ["袭","隰","舄","夏","先","鲜","咸","冼","洗","羡","线",
                           "相","香","襄","祥","向","相","项","肖","萧","孝",
                           "谢","渫","辛","忻","新","信","兴","星","刑","邢",
                           "行","幸","熊","修","须","顼","徐","许","旭","续",
                           "叶","伊","衣","依","仪","宜","乙","蚁","扆","弋","义",
                           "亦","易","弈","益","裔","翼","阴","殷","银","尹","印",
                           "应","英","营","赢","灜","雍","勇","涌","幽","尤","由",
                           "游","於","欲","余","鱼","俞","馀","宇","禹","庾","玉",
                           "郁","遇","喻","裕","毓","渊","元","袁","原","圆","源",
                           "员","苑","院","乐","岳","悦","越","云","妘","郧","运"]
        name = choice(first_name_list)+choice(second_name_list)+"85"
        # 输入Email 
        driver.find_element_by_name("email").send_keys(email)
        # 输入密码 
        driver.find_element_by_name("passwd").send_keys(password)
        # 输入确认密码 
        driver.find_element_by_name("repasswd").send_keys(password)
        # 输入姓名 
        driver.find_element_by_name("name").send_keys(name)
        # 随机男女性别 name sex and value 为1或0
        sex_list = ["0","1"]
        driver.find_element_by_xpath("//input[@name='sex' and @value='"+choice(sex_list)+"']").click()
        # 点击 选择地区 
        driver.find_element_by_xpath("//input[@value='选择地区']").click()
        sleep(1)
        # 点击 四川
        driver.find_element_by_link_text("四川").click()
        sleep(1)
        # 点击 成都市
        driver.find_element_by_link_text("成都市").click()
        sleep(1)
        # 点击 确定按钮 
        driver.find_element_by_xpath("//input[@value='确 定']").click()
        # 选择 隐私设置 
        # 方式一：直接点击
        driver.find_element_by_xpath("//select[@name='baseinfoprivacy']/option[@value='0']").click()
        # 方式二：通过Select类
#         select_element = driver.find_element_by_name("baseinfoprivacy")
#         sel = Select(select_element)
#         sel.select_by_value("0")
        # 方式三：一级一级找
#         driver.find_element_by_name("baseinfoprivacy").find_element_by_xpath("//option[@value='0']").click()
        # 点击 同意注册 
        driver.find_element_by_name("button").click()
        sleep(2)
        # 点击 基本资料
        driver.find_element_by_link_text("基本资料").click()
        sleep(1) 
        print("注册动作完成~~~~~~~~~~~~~~~~")      
        # 第四步：判断测试结果
        # 取得姓名输入框中的value属性的值 
        actual_name = driver.find_element_by_name("name").get_attribute("value")
        self.assertEqual(name, actual_name)
        print("判断测试结果完成~~~~~~~~~~~~~~~~")
    
    def tearDown(self):
        # 第五步：释放资源
        self.driver.quit()
        print("驱动释放完成~~~~~~~~~~~~~~~~")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()