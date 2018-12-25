import time,requests
from requests import sessions
from logging import exception
class Http_request:
    def __init__(self,url,method,params=None,headers=None,cookies=None):
        """heards需要进行该进"""
        try :
            if method.upper()=="GET":
                self.res=requests.get(url,params=params,cookies=cookies,headers=headers)
            elif method.upper()=="POST":
                self.res=requests.post(url,params=params,cookies=cookies,headers=headers)
        except Exception as e:
            raise e 
    def get_status_code(self):
        return self.res.status_code
    def get_json(self):
        return self.res.json()
    def get_cookiese(self):
        return self.res.cookies
    def get_text(self):
        return self.res.text
    def get_heards(self):
        """获取响应头部信息"""
        return self.res.headers
  




        