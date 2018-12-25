import configparser
from comm.get_project_path import Project_path
import os


conf_path=Project_path().project_path()+"conf"+os.sep+"web.conf"

con_info=configparser.ConfigParser()
con_info.read(conf_path,encoding="utf8")
print(con_info.sections())
print(con_info.options('Students'))
print(con_info.get('Students','name'))

class Read_conf():
    conf_path=Project_path().project_path()+"conf"+os.sep
    def __init__(self,path_name):
        self.conf_path=self.conf_path+path_name
    def read_conf(self):
        con_info=configparser.ConfigParser()
        con_info.read(self.conf_path,encoding="utf8")
        con_info.sections()
        con_info.options('Students')
        