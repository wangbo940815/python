from comm.http_request import Http_request
import unittest,requests
from ddt import ddt,unpack,data
from comm.DO_excel import Do_excel
from comm.log_decorator import log_decorator
from comm.basic_data import Replace_mobilephone,Context
from comm.connect_db import Connect_db
@ddt
class Http_test(unittest.TestCase):
    bidloan_data=Do_excel().read_excel("bidloan")
    def setUp(self):
        amount=Do_excel()
        amount_sql="select LeaveAmount from member where Id='23499'"
    @data(*bidloan_data)
    @log_decorator 
    def test_5bidloan(self,item):
        item.test_data=Replace_mobilephone().replace_mobile_info(item.test_data) #利用正则表达式处理数据
        if hasattr(Context, "cookies"):
            if item.expect["msg"]=="竞标成功":
                """ 竞标成功则去数据库判断用户金额是否跟投资金额匹配"""
                memberId=str(item.test_data["memberId"])
                begin_amount=(Connect_db().get_one("select LeaveAmount from member where Id='"+memberId+"'"))[0]  
                cookies=getattr(Context, "cookies")
                res=Http_request(item.url,item.method,params=item.test_data,cookies=cookies) 
               
                end_amount=(Connect_db().get_one("select LeaveAmount from member where Id='"+memberId+"'"))[0]  
                amount=item.test_data["amount"]
                self.assertEqual(begin_amount-amount,end_amount)
            else:
                cookies=getattr(Context, "cookies")
                res=Http_request(item.url,item.method,params=item.test_data,cookies=cookies) 
            
        else:
            res=Http_request(item.url,item.method,params=item.test_data)
            setattr(Context, "cookies", res.get_cookiese())
        actual=res.get_json()["code"]
        item.actual=actual
        self.assertEqual(actual,item.expect["code"])
        
        
        
        
        