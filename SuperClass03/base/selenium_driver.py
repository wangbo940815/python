# 封装Selenium相关方法，以便于提供回放速度的控制功能
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.read_config import get_browser_type,get_defalut_browser
from base.read_config import get_timeout,get_default_speed,get_except_speed

class SeleniumDriver(object):
    
    def __init__(self,browser=None,type=None):
        '''
                    初始化指定的浏览器驱动
        '''
        # 检查浏览器的类型是否支持，若为空则直接使用默认浏览器
        self.check_browser(browser)
        # 得到webdriver
        self.driver = self.get_webdriver()
        # 设置相应的智能等待时间
        self.set_timeout()
        # 获取放慢速度
        if type is None:
            self.speed = get_default_speed()
        else:
            self.speed = get_except_speed()
    
    def set_timeout(self):
        '''
                    此方法提供设置webdriver三种智能等待超时时间，根据配置文件进行时间的限定
        '''
        timeout = get_timeout()
        # 设置元素识别超时时间
        self.driver.implicitly_wait(timeout)
        # 设置页面加载超时时间
        self.driver.set_page_load_timeout(timeout)
        # 设置异步脚本加载超时时间
        self.driver.set_script_timeout(timeout)
    
    def get_webdriver(self):
        '''
                    此方法根据得到的浏览器类型拼接出webdriver所需具体的驱动，并执行实例化
        '''
        # 根据浏览器的类型进行实例化，得到实例化后的对象
        if "chrome" == str.lower(self.browser):
            driver = webdriver.Chrome()
        elif "firefox" == str.lower(self.browser):
            driver = webdriver.Firefox()
        elif "ie" == str.lower(self.browser):
            driver = webdriver.Ie()
        else:
            raise TypeError("获取驱动时，驱动类型未定义！！！")
        # 返回驱动变量
        return driver
        
    def check_browser(self,browser):
        # 如果未指定浏览器的类型则从配置文件中读取浏览器的参数
        if browser :
            # 不为空，则需要判断是否支持该类型的浏览器
            browser = str.capitalize(browser)
            browser_type_list = get_browser_type()
            if browser in browser_type_list:
                self.browser = browser
            else:
                raise TypeError("不支持该类型的浏览器，请检查！！支持的浏览器类型为：{}".format(browser_type_list))            
        else:
            # 为空，则读取配置文件默认类型
            self.browser = get_defalut_browser()

    def open(self,base_url):  
        # 调用webdriver真正相应的方法
        self.driver.get(base_url)  
        # 加个等待时间
        sleep(self.speed)
    
    def quit(self):  
        # 调用webdriver真正相应的方法
        self.driver.quit()  
              
    def find_element_by_id(self,id): 
        # 调用webdriver真正相应的方法
        self.driver.find_element_by_id(id)   
        # 加个等待时间
        sleep(self.speed)
        # 返回找到的元素对象
        return self.driver.find_element(by=By.ID, value=id)

    def find_element_by_name(self,name): 
        # 调用webdriver真正相应的方法
        self.driver.find_element_by_name(name)   
        # 加个等待时间
        sleep(self.speed)
        # 返回找到的元素对象
        return self.driver.find_element(by=By.NAME, value=name)
        
    def find_element_by_class_name(self,class_name): 
        # 调用webdriver真正相应的方法
        self.driver.find_element_by_class_name(class_name)   
        # 加个等待时间
        sleep(self.speed) 
        # 返回找到的元素对象
        return self.driver.find_element(by=By.CLASS_NAME, value=class_name)       
    
    def find_element_by_tag_name(self,tag_name): 
        # 调用webdriver真正相应的方法
        self.driver.find_element_by_tag_name(tag_name)   
        # 加个等待时间
        sleep(self.speed)  
        # 返回找到的元素对象
        return self.driver.find_element(by=By.TAG_NAME, value=tag_name)  
          
    def find_element_by_link_text(self,link_text): 
        # 调用webdriver真正相应的方法
        self.driver.find_element_by_link_text(link_text)   
        # 加个等待时间
        sleep(self.speed)
        # 返回找到的元素对象
        return self.driver.find_element(by=By.LINK_TEXT, value=link_text)  
        
    def find_element_by_partial_link_text(self,partial_link_text): 
        # 调用webdriver真正相应的方法
        self.driver.find_element_by_partial_link_text(partial_link_text)   
        # 加个等待时间
        sleep(self.speed)
        # 返回找到的元素对象
        return self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value=partial_link_text)  
        
    def find_element_by_xpath(self,xpath): 
        # 调用webdriver真正相应的方法
        self.driver.find_element_by_xpath(xpath)   
        # 加个等待时间
        sleep(self.speed) 
        # 返回找到的元素对象
        return self.driver.find_element(by=By.XPATH, value=xpath)        

    def find_element_by_css_selector(self,css_selector): 
        # 调用webdriver真正相应的方法
        self.driver.find_element_by_css_selector(css_selector)   
        # 加个等待时间
        sleep(self.speed) 
        # 返回找到的元素对象
        return self.driver.find_element(by=By.CSS_SELECTOR, value=css_selector)  
        
        
        
        
               