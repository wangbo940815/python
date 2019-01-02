import   os
'''存放框架类的 日志，报告，配置文件的路径，保证项目的可移植性，尽量不要使用os.getcwd()去获取路径
，此方法在其他方法调用时，路径会发生变化，会产生错误'''


'''获取项目路径'''
file_path=os.path.abspath(__file__)
project_path=os.path.dirname(os.path.dirname(file_path))
"""配置文件路径"""
conf_path=project_path+os.sep+"conf/"
'''测试用例路径'''
test_case_path=project_path+os.sep+"test_case"
"""生成html报告路径"""
html_path=project_path+os.sep+"test_result/html_result"
"""生成log日志路径"""
log_path=project_path+os.sep+"test_result/log_result"
"""测试数据存放路径"""
data_path=project_path+os.sep+"test_data/testdatas.xlsx"