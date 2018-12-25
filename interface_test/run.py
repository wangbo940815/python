import  unittest,os,time
from comm.HTMLTestRunnerNew import HTMLTestRunner
from comm.DO_excel import *
from test_case import http_request_case
from comm import constans


if __name__ == '__main__':
    file_path=constans.html_path+os.sep
    name=time.strftime("%Y_%m_%d_%H_%M_%S")+".html"
    file_path=file_path+name
    suite=unittest.TestSuite()
    loader=unittest.TestLoader()
    suite.addTest(loader.loadTestsFromModule(http_request_case))
    print(file_path)
    with open(file_path,"wb+") as file:
        runner=HTMLTestRunner(stream=file,title="WEB自动化测试报告",description="执行情况如下",
                              )
        runner.run(suite)

   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

