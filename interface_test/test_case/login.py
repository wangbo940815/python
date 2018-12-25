from comm.http_request import Http_request
import unittest,requests
from ddt import ddt,unpack,data
from comm.DO_excel import Do_excel
from comm.log_decorator import log_decorator
from comm.basic_data import Replace_mobilephone
mobilephone_sql="select mobilephone from member where  not mobilephone is null order by mobilephone desc limit 1"
@ddt
class Http_test(unittest.TestCase):
    login_data=Do_excel().read_excel("login")
    mobilephone_sql="select mobilephone from member where  not mobilephone is null order by mobilephone desc limit 1"
    def setUp(self):
        self.phone=Replace_mobilephone(mobilephone_sql)
    @data(*login_data)
    @log_decorator 
    def test_2login(self,item):
        item.test_data=self.phone.replace_mobile_info(item.test_data) #利用正则表达式处理数据
        res=Http_request(item.url,item.method,params=item.test_data) 
        actual=res.get_json()["msg"]
        item.actual=actual
        self.assertEqual(actual,item.expect["msg"])
        
        
        
        