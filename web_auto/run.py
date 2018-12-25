from test_case import Think_sns
import unittest,os,time
from comm.HTMLTestRunnerNew import HTMLTestRunner




if __name__ == '__main__':
    suite=unittest.TestSuite()
    loader=unittest.TestLoader()
    suite.addTest(loader.loadTestsFromModule(Think_sns))
    file_path=os.getcwd()+os.sep+"test_result"+os.sep+"html_result"+os.sep
    name=time.strftime("%Y_%m_%d_%H_%M_%S")+".html"
    file_path=file_path+name
    with open(file_path,"wb+") as file:
        runner=HTMLTestRunner(stream=file,title="WEB自动化测试报告",description="执行情况如下",
                              )
        runner.run(suite)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    