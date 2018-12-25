import   os
'''获取项目路径'''
file_path=os.path.abspath(__file__)
project_path=os.path.dirname(os.path.dirname(file_path))
"""配置文件路径"""
conf_path=project_path+os.sep+"conf/"
"""生成html报告路径"""
html_path=project_path+os.sep+"test_result/html_result"
"""生成log日志路径"""
log_path=project_path+os.sep+"test_result/log_result"
"""测试数据存放路径"""
data_path=project_path+os.sep+"test_data/testdatas.xlsx"