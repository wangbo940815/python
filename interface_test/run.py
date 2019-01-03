import  unittest,os,time
from comm.HTMLTestRunnerNew import HTMLTestRunner
from comm.DO_excel import *
from test_case import *
from comm import constans

'''根据模糊匹配收集测试用例，生存测试报告，报告形式有HTMLTESTreport这个py文件决定，可在网上下载其他，调用即可'''
if __name__ == '__main__':
    file_path=constans.html_path+os.sep
    name="interface_report.html"
    file_path=file_path+name
#     suite=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(constans.test_case_path, "test_*.py")
    loader=unittest.TestLoader()

    with open(file_path,"wb+") as file:
        runner=HTMLTestRunner(stream=file,title="接口自动化测试报告",description="执行情况如下",
                              )
        runner.run(discover)

   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

