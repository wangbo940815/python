import time,requests
from requests import sessions
from logging import exception
class Http_request:
    '''http请求类，主要把requests三方包进行封装，主要需要传入参数为URL，cookies，请求数据data或者params，2者差别自己百度
               ，headers可以根据接口文档选择性配置，，在需要验权，和有浏览器限制或者接口文档要求时，需要自己封装一个请求头，这时需要
            传入headers'''
    def __init__(self,url,method,params=None,headers=None,cookies=None):
        '''封装了post和 get方法，其他方法可以添加'''
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
  




        