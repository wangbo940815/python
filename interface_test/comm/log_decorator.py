from comm.my_log import *
import os,sys,time
from comm.DO_excel import Do_excel
def log_decorator(fun):
    '''日志装饰器类，穿入的参数fun是一个函数，是函数，而在方法new_name(*kwg)中的*kwg是传入函数fun本身的参数，在调用的
    地方可以看到kwg相当于self（类的对象），和item，到具体的测试用例中查看这个参数
   该装饰器主要作用是把每个测试用例类中方法要用到的共同方法封装，减少代码量。
   在此处：1.实现根据不同测试 类和方法名建立日志文件名字
       2.检查fun函数的参数，作为日志输出，方便问题定位
       3.回写测试结果'''
    write_excel=Do_excel()
    def new_name(*kwg):
        """获取类名"""
        class_name = str(kwg[0].__class__)
        class_name=class_name .split("'")[1]
        funct_name = str(kwg[0]).split("=")[0].split(" ")[0]
        moudle_name=class_name+"_"+funct_name
        '''根据不同的测试类名字出给日志收集类，使得根据不同的测试类名新建不同的日志文件'''
        log=Record_logging(funct_name.split("_")[1],get_moudle_name=moudle_name[0:-2]) 
        log.info('测试用例{}开始执行'.format(moudle_name))  
        
        try:  
            begin_time=time.clock()
            fun(*kwg)
            
            Result="Pass"
        except AssertionError as e:
            Result="Fail"
            raise e
        finally: 
            end_time=time.clock()
            '''日志输出请求信息'''
            log.info('你请求的URL地址是:{}'.format(kwg[1].url)) 
            log.info('你的请求方式是:{}'.format(kwg[1].method)) 
            log.info('你的请求参数是:{}'.format(kwg[1].test_data)) 
            log.info('你的预期结果是:{}'.format(kwg[1].expect["code"]))  
            log.info('请求的实际结果是:{}'.format(kwg[1].actual))
            if Result=="Pass":
                log.info('测试用例开始执行的结果是:{}'.format(Result))
            else:
                log.error('测试用例开始执行的结果是:{}'.format(Result))  
                '''回写测试结果'''
            write_excel.write_excel(kwg[1].sheet_name,kwg[1].id+1,7,kwg[1].actual)
            write_excel.write_excel(kwg[1].sheet_name,kwg[1].id+1,8,Result)
            log.info('测试用例{}结束执行,一共执行{}'.format(moudle_name,end_time-begin_time))
    return new_name

