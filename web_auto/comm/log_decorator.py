from comm.my_log import *
import os,sys,time
import inspect
def log_decorator(fun):
    
    def new_name(*kwg):
        begin_time=time.clock()

        end_time=time.clock()
        """获取类名"""
        class_name = str(kwg[0].__class__)
        class_name=class_name .split("'")[1]
        funct_name = str(kwg[0]).split("=")[0].split(" ")[0]
        moudle_name=class_name+"_"+funct_name
        log=Record_logging(class_name,get_moudle_name=moudle_name) 
        log.info('测试用例{}在{}开始执行'.format(moudle_name,begin_time))       
        fun(*kwg)

        log.info('测试用例{}在{}结束执行,一共执行{}'.format(moudle_name,end_time,end_time-begin_time))

    return new_name

