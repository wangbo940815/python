# 此模块提供读取配置文件相关操作
from xml.dom.minidom import parse

def read_ip_info():
    '''
            此方法提供读取配置文件中IP相关的信息
    '''
    # 定义用于存储ip信息的字典
    ip_dict = {}
    # 解析xml文件
    dom = parse("../conf/config.xml")
    # 得到根节点元素
    document = dom.documentElement
    # 得到根节点下级所有的ipinfo元素，注意返回类型为元素列表
    ipinfo_list = document.getElementsByTagName("ipinfo")
    # 整个配置文件中只有一个ipinfo，所以指定读取第一个，同样返回的是元素列表
    ip_list = ipinfo_list[0].getElementsByTagName("ip")
    port_list = ipinfo_list[0].getElementsByTagName("port")
    protocol_list = ipinfo_list[0].getElementsByTagName("protocol")
    # 得到具体的子节点信息，childNodes方法会返回一个装有子节点元素的列表
    ip = ip_list[0].childNodes[0].data
    port = port_list[0].childNodes[0].data
    protocol = protocol_list[0].childNodes[0].data
    # 返回ip及端口
    ip_dict["ip"] = ip
    ip_dict["port"] = port
    ip_dict["protocol"] = protocol
    return ip_dict

def read_db_info():
    '''
            此方法提供读取配置文件中数据库相关的信息
    '''
    # 定义用于存储db信息的字典
    db_dict = {}
    # 解析xml文件
    dom = parse("../conf/config.xml")
    # 得到根节点元素
    document = dom.documentElement
    # 得到根节点下级所有的dbinfo元素，注意返回类型为元素列表
    dbinfo_list = document.getElementsByTagName("dbinfo")
    # 整个配置文件中只有一个dbinfo，所以指定读取第一个，同样返回的是元素列表
    dbname_list = dbinfo_list[0].getElementsByTagName("dbname")
    dbuser_list = dbinfo_list[0].getElementsByTagName("dbuser")
    dbpasswd_list = dbinfo_list[0].getElementsByTagName("dbpasswd")
    # 得到具体的子节点信息，childNodes方法会返回一个装有子节点元素的列表
    dbname = dbname_list[0].childNodes[0].data
    dbuser = dbuser_list[0].childNodes[0].data
    dbpasswd = dbpasswd_list[0].childNodes[0].data
    # 返回ip及端口
    db_dict["dbname"] = dbname
    db_dict["dbuser"] = dbuser
    db_dict["dbpasswd"] = dbpasswd
    return db_dict

def get_ip_info():
    '''
            此方法提供拼接IP信息的功能
    '''
    # 先调用读取ip信息的方法
    ip_dict = read_ip_info()
    protocol = ip_dict.get("protocol")
    ip = ip_dict.get("ip")
    port = ip_dict.get("port")
    # 返回ipinfo
    ipinfo = protocol+"://"+ip+":"+port
    return ipinfo

def read_browser_info():
    '''
            此方法提供读取配置文件中浏览器驱动相关的信息
    '''
    # 定义用于存储browser信息的字典
    browser_dict = {}
    # 解析xml文件
    dom = parse("../conf/config.xml")
    # 得到根节点元素
    document = dom.documentElement
    # 得到根节点下级所有的browserinfo元素，注意返回类型为元素列表
    browser_info_list = document.getElementsByTagName("browserinfo")
    # 整个配置文件中只有一个browserinfo，所以指定读取第一个，同样返回的是元素列表
    default_list = browser_info_list[0].getElementsByTagName("default")
    type_list = browser_info_list[0].getElementsByTagName("type")
    # 得到具体的子节点信息，childNodes方法会返回一个装有子节点元素的列表
    default = default_list[0].childNodes[0].data
    type = type_list[0].childNodes[0].data
    # 处理type将其变为列表，并做首字母大写处理
    type_list = type.split(",")
    for t in type_list:
        i = type_list.index(t)
        t = str.capitalize(t)
        type_list[i] = t
    # 将字符串进行首字母大写处理
    default = str.capitalize(default)
    # 返回浏览器默认类型和支持类型
    browser_dict["default"] = default
    browser_dict["type"] = type_list
    return browser_dict    

def get_defalut_browser():
    '''
            此方法提供获取默认浏览器的功能
    '''
    browser_dict = read_browser_info()
    return browser_dict["default"]

def get_browser_type():
    '''
            此方法提供获取浏览器类型列表的功能
    '''
    browser_dict = read_browser_info()
    return browser_dict["type"]

def get_timeout():
    '''
            此方法提供读取配置文件中智能等待时间的信息
    '''
    # 解析xml文件
    dom = parse("../conf/config.xml")
    # 得到根节点元素
    document = dom.documentElement
    # 得到根节点下级所有的timeout元素，注意返回类型为元素列表
    timeout_list = document.getElementsByTagName("timeout")
    # 得到具体的子节点信息，childNodes方法会返回一个装有子节点元素的列表
    timeout = timeout_list[0].childNodes[0].data
    # 返回超时时间
    return int(timeout) 
   
def get_default_speed():
    '''
            此方法提供读取配置文件中智能等待时间的信息
    '''
    # 解析xml文件
    dom = parse("../conf/config.xml")
    # 得到根节点元素
    document = dom.documentElement
    # 得到根节点下级所有的speed元素，注意返回类型为元素列表
    speed_list = document.getElementsByTagName("defaultspeed")
    # 得到具体的子节点信息，childNodes方法会返回一个装有子节点元素的列表
    defaultspeed = speed_list[0].childNodes[0].data
    # 返回超时时间
    return int(defaultspeed)

def get_except_speed():
    '''
            此方法提供读取配置文件中智能等待时间的信息
    '''
    # 解析xml文件
    dom = parse("../conf/config.xml")
    # 得到根节点元素
    document = dom.documentElement
    # 得到根节点下级所有的speed元素，注意返回类型为元素列表
    speed_list = document.getElementsByTagName("exceptspeed")
    # 得到具体的子节点信息，childNodes方法会返回一个装有子节点元素的列表
    exceptspeed = speed_list[0].childNodes[0].data
    # 返回超时时间
    return int(exceptspeed)
   
# print(read_ip_info())
# print(read_db_info())
# print(read_browser_info())
