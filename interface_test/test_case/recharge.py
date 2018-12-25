from comm.http_request import Http_request
import unittest,requests
from ddt import ddt,unpack,data
from comm.DO_excel import Do_excel
from comm.log_decorator import log_decorator
from comm.basic_data import Replace_mobilephone,Context
mobilephone_sql="select mobilephone from member where  not mobilephone is null order by mobilephone desc limit 1"
@ddt
class Http_test(unittest.TestCase):
    recharge_data=Do_excel().read_excel("recharge")
    mobilephone_sql="select mobilephone from member where  not mobilephone is null order by mobilephone desc limit 1"
    money_sql="select leaveAmont from member where mobilephone=''"
    def setUp(self):
        self.phone=Replace_mobilephone(mobilephone_sql)
        
    @data(*recharge_data)
    @log_decorator 
    def test_3recharge(self,item):
        item.test_data=self.phone.replace_mobile_info(item.test_data) #利用正则表达式处理数据
        if hasattr(Context, "cookies"):
            cookies=getattr(Context, "cookies")
            res=Http_request(item.url,item.method,params=item.test_data,cookies=cookies) 
        else:
            res=Http_request(item.url,item.method,params=item.test_data)
            setattr(Context, "cookies", res.get_cookiese())
        actual=res.get_json()["msg"]
        item.actual=actual
        self.assertEqual(actual,item.expect["msg"])
        
        
        
        