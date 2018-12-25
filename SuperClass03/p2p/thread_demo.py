'''
 threading库   多线程
'''

from time import ctime, sleep

import threading


#听音乐
def music(mus):
    print("我正在听  {} 音乐——>{}".format(mus,ctime()))
    sleep(5)
    print("音乐结束——>{}".format(ctime()))

#看电影
def movie(mov):
    print("我正在看 {} 电影——>{}".format(mov,ctime()))
    sleep(2)
    print("电影结束——>{}".format(ctime()))
    
#创建线程组
threads=[]

#创建线程t1  ,调用music方法target=music
t1 = threading.Thread(target=music,args=("彩虹",))
#将线程t1加到线程组中
threads.append(t1)
#创建线程t2
t2=threading.Thread(target=movie,args=("蜘蛛侠3",))
#将线程t2加到线程组中
threads.append(t2)


if __name__=='__main__':
    

          
    for t in threads:   #通过for循环遍历线程组  [t1,t2]
        #t.setDaemon(True)   #守护线程，必须在start()之前设置，如果不设置为守护线程，程序会被无限挂起。
        #开始线程活动
        t.start()
        #print(t.isAlive())
#     print(t.getName())
#     t.join()  #必须等待for循环内的2个进程都结束后，才会去执行主线程
    i=1
    while len(threads) != 0:
        for t in threads:
            if not (t.is_alive()) :
                threads.remove(t)
        print("第{}次检查".format(i))
        i+=1
        sleep(1)
    #join()方法用于等待线程终止，作用： 在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
        
    print("all over——>{}".format(ctime()))  #这是主线程
