# 设置网页的flash相关操作
from time import sleep
import jpype

def set_flash(driver,base_url,project_path):
    '''
            该方法提供设置flash为允许的功能
    '''
    # 定义所需图片在项目中的位置
    picture_path = project_path+r"images\sikuli_img\chrome_set"
    # 打开flash的设置页
    driver.get("chrome://settings/content/flash")
    sleep(2)
    # 定义jvm的路径及jar的路径
    jvm_path = r"C:\Program Files\Java\jdk1.8.0_151\jre\bin\server\jvm.dll"
    jar_path = "-Djava.class.path="+project_path+r"libs\sikulixapi.jar"
    print(jar_path)
    # 启动JVM
    jpype.startJVM(jvm_path,jar_path)
    # 得到Screen类和Pattern类
    Screen = jpype.JClass("org.sikuli.script.Screen")
    Pattern = jpype.JClass("org.sikuli.script.Pattern")
    # 实例化Screen类
    screen = Screen()
    # 先定义添加图片的路径，然后进行适当的偏移
    add_path = picture_path+r"\add.png"
    offset_Path = Pattern(add_path).targetOffset(300,0)
    screen.click(offset_Path)
    sleep(2)
    # 输入网址
    url_path = picture_path+r"\url.png"
    screen.type(url_path,base_url)
    # 点击添加
    add_ok_path = picture_path+r"\add_ok.png"
    screen.click(add_ok_path)
    # 关闭JVM
    jpype.shutdownJVM()
    sleep(1)
    
    
    
    
    
    
    
    
    
    
    
    