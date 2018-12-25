# 此模块提供异常重试和日志记录修饰符的方法

def specifier(func):
    '''
            此方法提供日志记录和异常重试判断的功能
    '''
    print(func)
    print("{} 正在执行中~~~~~".format(func.__name__))
    def f(*xx):
        print(xx)
        try:
            t = func(*xx)
        except Exception as e:
            print("{} 正在执行过程中出异常啦：{}".format(func.__name__,str(e)))
        else:
            print("{} 执行完成~~~~~".format(func.__name__))
            return t
    return f