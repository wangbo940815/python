from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium import webdriver
from comm.my_log import *
import time,os
class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()#最大显示窗口
        self.log=Record_logging("basepage")
        print("BasePAGE实例化log模块")
        """函数等待要定位的页面元素加载，超时则报错，在规定时间内加载完毕继续执行下一步"""
    def element_visibil(self,locater,locater_style=By.XPATH,wait_time=40,interval=0.5):  #located_style,定位方式，located定位元素
        if locater_style not in By.__dict__.values():
            self.log.info("定位类型{}不在支持范围内，清重新输入".format(locater_style))
            raise InvalidSelectorException
        try:
            find_elelment_begin=time.time()
            WebDriverWait(self.driver,wait_time,interval).until(EC.visibility_of_element_located((locater_style,locater)))
            find_elelment_end=time.time()
            find_waste_time=float(find_elelment_end)-float(find_elelment_begin)
            self.log.info("在页面中查找元素{}，在{}开始，在{}结束，花费时间{}".format(locater,find_elelment_begin,find_elelment_end,find_waste_time))
        except TimeoutError as e:
            self.save_screen("element_visibil查找页面元素超时")
            self.log.error("查找页面元素超时")
            raise e
       
    def element_exist(self,locater,locater_style=By.XPATH,wait_time=40,interval=0.5):  #located_style,定位方式，located定位元素
        if locater_style not in By.__dict__.values():
            self.log.info("定位类型{}不在支持范围内，清重新输入".format(locater_style))
        try:
            find_elelment_begin=time.time()
            WebDriverWait(self.driver,wait_time,interval).until(EC.presence_of_element_located((locater_style,locater)))
            find_elelment_end=time.time()
            find_waste_time=float(find_elelment_begin)-float(find_elelment_end)
            self.log.info("在页面中查找元素{}，在{}开始，在{}结束，花费时间{}".format(locater,find_elelment_begin,find_elelment_end,find_waste_time))
        except TimeoutError as e:
            self.save_screen("element_exist查找页面元素超时")
            self.log.error("查找页面元素超时")
            raise e        
    def save_screen(self,name=None):   
        shoot_time=time.strftime("%Y_%m_%d,%H_%M_%S")
        file_path=r"C:\Users\Administrator.BF-20180623OAFS\workspace\web_auto\test_result"+os.sep+"shootscreen_picture"+os.sep+name+shoot_time+".png"
        print(file_path)
        self.driver.save_screenshot(file_path)
        """进行适当的修改，让输出的图片中包含使用该函数的测试用例名称"""
        self.log.info("截取当前页面，保存路径为{}".format(file_path))
    
    
    """该函数提供alert弹出窗口处理"""
    def alert_handle(self,action="accept",wait_time=40,interval=0.5):
        try:
            WebDriverWait(self.driver,wait_time,interval).until(EC.alert_is_present())
        except TimeoutError as e:
            self.save_screen()
            raise e
        alert=self.driver.switch_to_alert()
        message=alert.alert_text
        if action=="accept":
            alert.accept()
        else:
            alert.dismiss()
        return message
    """函数处理frame窗口切换和处理"""
    def frame_in(self,frame_name=None,frame_xpath=None,wait_time=40,interval=0.5):
        if frame_name==None and frame_xpath==None:
            print("frame_name和frame_xpath，这2个参数不能同时为空,请重新输入")
            return -1   #可能有错误
        elif frame_name!=None:
            WebDriverWait(self.driver,wait_time,interval).until(EC.frame_to_be_available_and_switch_to_it(frame_name))
        else:
            frame=self.driver.find_element_by_xpath(frame_xpath)
            self.driver.switch_to_frame(frame)
    def get_element(self,locater,locater_style=By.XPATH,wait_time=40,interval=0.5,type='visible'):  
        if type=="visible":
            self.element_visibil(locater,locater_style,wait_time,interval)
        else:
            self.element_exist(self,locater,locater_style,wait_time,interval)
            
        try:
            ele=self.driver.find_element(locater_style,locater)
            return ele
        except NoSuchElementException as e: 
            self.save_screen("NoSuchElement")
            print(e)
            raise e
        
            

