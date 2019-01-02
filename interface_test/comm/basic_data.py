from comm.connect_db import Connect_db
from comm.read_conf import Read_conf
import re,json

class Context:
    '''上下文处理类，可以用于存放数据
    主要作用是利用反射机制，存放临时数据，例如登录后的cookies  利用setattr方法存储cookies后在用getattr获取
    '''
    basci_data=Read_conf()
    mobilephone=basci_data.get("basic", "login_user")
    pwd=basci_data.get("basic", "login_password")
    memberId=str((Connect_db().get_one("select Id from member where mobilephone='"+mobilephone+"'"))[0])
    
    
    
    
class Replace_mobilephone:
    '''数据替换类，为了保证一些数据的重用性，例如注册（一个号码被注册后不能被重复注册）
            可以在请求数据中定义一种规则例如：{register_phoneIsNew}，出现这种规则表示要使用一个新的号码
            ，此处我使用在数据库中差已经注册的号码加1的方式，去获取没有被注册的号码，保证重用性（必要时需要添加号码规则校验）
    ，其余类似数据可以用相同方法处理
    
    '''
    mobilephone_sql="select mobilephone from member where  not mobilephone is null order by mobilephone desc limit 1"
    NewmemberId_sql="select  *  from member order by Id DESC LIMIT 1"
    loanId_IsNew_sql='select * from loan order by Id desc'
    loanId_StatusError_sql="select * from loan where not FullTime  is null"
    loanId_IsEnough_sql='select * from loan where not FullTime  is null '
    
    def get_new(self,sql):
        data=(Connect_db().get_one(sql))[0]
        return str(int(data)+1)
    def get_loanId(self,sql):
        data=(Connect_db().get_one(sql))[0]
        return data
    
    def replace_mobile_info(self,target):
        pattern="\$\{(.*?)\}"
        match_ob=re.search(pattern, target)
        if match_ob:#根据规则在目标对象中查找，返回一个对象
            key=match_ob.group(1) 
            
            if key=="register_phoneIsNew" :#用于注册的账号，并且注册成功
                target=re.sub(pattern,self.get_new(self.mobilephone_sql), target, count=1)
                return json.loads(target)
            elif key==  "memeberId_IsNew" :
                target=re.sub(pattern,self.get_new(self.NewmemberId_sql), target, count=1)
                return json.loads(target)                
            elif key=="mobilephone":
                while   re.search(pattern, target): 
                    match_ob=re.search(pattern, target)#根据规则在目标对象中查找，返回一个对象
                    key=match_ob.group(1)             #根据分组选取值
                    info=getattr(Context,key) 
                    '''利用规则替换掉目标对象的值，将替换后的值赋值给目标，是目标所有满足正则的全部被替换''' 
                    target=re.sub(pattern,info, target, count=1)#count=1一次只替换一个
                return json.loads(target)
            elif key=="memberId":
                while   re.search(pattern, target): 
                    match_ob=re.search(pattern, target)         #根据规则在目标对象中查找，返回一个对象
                    key=match_ob.group(1) 
                #根据分组选取值
                    if key==  "loanId_IsNew":
                        target=re.sub(pattern,self.get_new(self.loanId_IsNew_sql), target, count=1)
                    elif key=="loanId_StatusError":
                        target=re.sub(pattern,self.get_new(self.loanId_StatusError_sql), target, count=1)
                    elif key=="loanId_IsEnough":
                        target=re.sub(pattern,self.get_new(self.loanId_IsEnough_sql), target, count=1)
                    else:
                        info=getattr(Context,key)
                    
                        '''利用规则替换掉目标对象的值，将替换后的值赋值给目标，是目标所有满足正则的全部被替换''' 
                        target=re.sub(pattern,info,target,count=1)
                return json.loads(target)

        else:
            return json.loads(target)
            
        
        
        
        
if __name__ == '__main__':
    p='{"mobilephone":"${mobilephone}","password":"${pwd}"}'
    {"mobilephone":"${register_phoneIsNew}","pwd":"1234567890"}
