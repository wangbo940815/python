import logging,os,time
from comm.get_project_path import *
from nt import mkdir
moudle=""
new_name=""
class Record_logging():

    def __init__(self,name=None,get_moudle_name=None,cmd_level=logging.DEBUG,file_level=logging.DEBUG):
        self.name=name
        self.cmd_level=cmd_level
        self.file_level=file_level 
        
        
        if name!=None:
            global new_name
            new_name=name
        if get_moudle_name!=None:
            global moudle
            moudle=get_moudle_name
 
        """设置日志路径"""
        now_date=time.strftime('%Y_%m_%d')
        path=Project_path().project_path()+"test_result"+os.sep+'log'+os.sep+now_date
        if not os.path.isdir(path):
            mkdir(path)
            
        file_path=path+os.sep+moudle+".txt" 
        
        """初始化"""
        self.logger=logging.getLogger(self.name)   
        self.logger.setLevel(logging.DEBUG)
        """制定统一的输出格式:%(levelname)s 文本形式的日志级别
        %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
        %(message)s  %(message)s 用户输出的消息"""
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y_%m_%d %H_%M_%S')
        
        """设置控制台日志"""
        cmd_h=logging.StreamHandler()
        cmd_h.setLevel(self.cmd_level)
        cmd_h.setFormatter(fmt)
        """设置文件日志"""
        file_h=logging.FileHandler(file_path,encoding="utf8")  #指定日志路径
        file_h.setLevel(self.file_level)
        file_h.setFormatter(fmt)
        
        """添加2种日志"""
        self.logger.addHandler(cmd_h)
        self.logger.addHandler(file_h)

        
    def debug(self,message):
        self.logger.debug(message)
        
    def info(self,message):
        self.logger.info(message)
        
    def warning(self,message):
        self.logger.warning(message)
    def error(self,message):
        self.logger.error(message)
    def Log_critical(self,message):
        self.logger.critical(message)

