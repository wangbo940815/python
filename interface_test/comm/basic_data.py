from comm.connect_db import Connect_db
from comm.read_conf import Read_conf
import re,json

class Context:
    basci_data=Read_conf()
    mobilephone=basci_data.get("basic", "login_user")
    pwd=basci_data.get("basic", "login_password")


class Replace_mobilephone:
    def __init__(self,sql=None):
        self.sql=sql   
    def replace_mobile_info(self,target):
        pattern="\$\{(.*?)\}"
        match_ob=re.search(pattern, target)
        if match_ob:#根据规则在目标对象中查找，返回一个对象
            key=match_ob.group(1) 
            print(key)
            if key=="register_phoneIsNew":#用于注册的账号，并且注册成功
                data=(Connect_db().get_one(self.sql))[0]
                print(data)
                new_mobilephone=str(int(data)+1)
                print(new_mobilephone)
                target=re.sub(pattern,new_mobilephone, target, count=1)
                print(target)
                return json.loads(target)
            elif key=="mobilephone":
                while   re.search(pattern, target): 
                    match_ob=re.search(pattern, target)#根据规则在目标对象中查找，返回一个对象
                    key=match_ob.group(1)             #根据分组选取值
                    info=getattr(Context,key)  
                    '''利用规则替换掉目标对象的值，将替换后的值赋值给目标，是目标所有满足正则的全部被替换''' 
                    target=re.sub(pattern,info, target, count=1)#count=1一次只替换一个
                return json.loads(target)
        else:
            return json.loads(target)
            
        
        
        
        
if __name__ == '__main__':
    p='{"mobilephone":"${mobilephone}","password":"${pwd}"}'
    a=Replace_mobilephone("select mobilephone from member where  not mobilephone is null order by mobilephone desc limit 1").replace_login_info(p)
    print(a)