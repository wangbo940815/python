import logging,os,time
from nt import mkdir
from comm.read_conf import Read_conf
from comm import constans
moudle=""
new_name=""
class Record_logging():

    def __init__(self,name=None,get_moudle_name=None):
        self.name=name
        
        
        """读取关于log的配置文件信息，包含日志输出路径，日志收集器收集级别，日志渠道输出级别，日志输出格式formmat"""
        self.log_set=Read_conf()
        self.log_ouyput_level=self.log_set.get("log","log_output_level")
        self.log_level=self.log_set.get("log","log_get_level")
        self.log_formatter=self.log_set.get("log","log_formatter")
        
        if name!=None:
            global new_name
            new_name=name
        if get_moudle_name!=None:
            global moudle
            moudle=get_moudle_name
        """设置日志路径"""
        now_date=time.strftime('%Y_%m_%d')
        path=constans.log_path+os.sep+now_date
        if not os.path.isdir(path):
            mkdir(path)    
        file_path=path+os.sep+moudle+".txt" 
        """初始化"""
        
        self.logger=logging.getLogger(self.name)   
        self.logger.setLevel(self.log_level)
        
        if not self.logger.handlers:
            """制定统一的输出格式:%(levelname)s 文本形式的日志级别
            %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
            %(message)s  %(message)s 用户输出的消息"""
            fmt = logging.Formatter(self.log_formatter)
            """设置控制台日志"""     
            cmd_h=logging.StreamHandler()
            cmd_h.setLevel(self.log_ouyput_level)
            cmd_h.setFormatter(fmt)
            """设置文件日志"""
            file_h=logging.FileHandler(file_path,encoding="utf8")  #指定日志路径
            file_h.setLevel(self.log_ouyput_level)
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
