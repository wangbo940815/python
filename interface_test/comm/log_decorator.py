from comm.my_log import *
import os,sys,time
from comm.DO_excel import Do_excel
def log_decorator(fun):
    write_excel=Do_excel()
    def new_name(*kwg):
        begin_time=time.clock()
        end_time=time.clock()
        """获取类名"""
        class_name = str(kwg[0].__class__)
        class_name=class_name .split("'")[1]
        funct_name = str(kwg[0]).split("=")[0].split(" ")[0]
        moudle_name=class_name+"_"+funct_name
        
        log=Record_logging(funct_name.split("_")[1],get_moudle_name=moudle_name[0:-2]) 
        log.info('测试用例{}开始执行'.format(moudle_name))  
        try:  
            fun(*kwg)
            Result="Pass"
        except AssertionError as e:
            Result="Fail"
            raise e
        finally: 
            log.info('你请求的URL地址是:{}'.format(kwg[1].url)) 
            log.info('你的请求方式是:{}'.format(kwg[1].method)) 
            log.info('你的请求参数是:{}'.format(kwg[1].test_data)) 
            log.info('你的预期结果是:{}'.format(kwg[1].expect["msg"]))  
            log.info('请求的实际结果是:{}'.format(kwg[1].actual))
            if Result=="Pass":
                log.info('测试用例开始执行的结果是:{}'.format(Result))
            else:
                log.error('测试用例开始执行的结果是:{}'.format(Result))  
            write_excel.write_excel(kwg[1].sheet_name,kwg[1].id+1,7,kwg[1].actual)
            write_excel.write_excel(kwg[1].sheet_name,kwg[1].id+1,8,Result)
            log.info('测试用例{}结束执行,一共执行{}'.format(moudle_name,end_time-begin_time))
    return new_name

