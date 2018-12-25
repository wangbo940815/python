from configparser import ConfigParser
import os 
from comm import constans
class Read_conf():
    def __init__(self):
        self.conf_path=constans.conf_path+"switch.conf"
        self.read()
        if self.getboolean("switch", "ON"):
            self.conf_path=constans.conf_path+"setting.conf"
            self.read()
        else :
            self.conf_path=constans.conf_path+"setting2.conf"
            self.read()
    def read(self):
        self.conf_info=ConfigParser()
        self.conf_info.read(self.conf_path,encoding="utf8")
    def get(self,section,option):
        return self.conf_info.get(section,option)
    def getboolean(self,section,option):
        return self.conf_info.getboolean(section, option)
    def getfloat(self,section,option):
        return self.conf_info.getfloat(section, option)
    def getint(self,section,option):
        return self.conf_info.getint(section, option)
