import threading
import time
# 多线程模块threading

# 1.1 threading方法
# threading.currentThread(): 返回当前的线程变量。
# threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

# 1.2 threading.Thread类
# run(): 用以表示线程活动的方法。
# start():启动线程活动。
# join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
# isAlive(): 返回线程是否活动的。
# getName(): 返回线程名。
# setName(): 设置线程名。

#1.3 线程同步

# 使用 threading.Lock() 和 threading.Rlock() 可以实现简单的线程同步，
# 这两个对象都有 acquire 方法和 release 方法，对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间。


class myThread(threading.Thread) :
    def __init__(self,threadId,name,delay):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.delay = delay
    def run(self):
        print ("开始线程：" + self.name, end="\n")
        threadLock.acquire()
        print_time(self.name, self.delay, 5)
        threadLock.release()
        print ("退出线程：" + self.name)

exit_tag = 0
threadLock = threading.Lock()
threads = []

def print_time(threadName,delay,counter) :
    while counter:
        if exit_tag :
            threadName.exit()
        time.sleep(delay)
        print(f"{threadName}: {time.ctime(time.time())}")
        counter-=1
# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
threads.append(thread1)
threads.append(thread2)
for t in threads:
    t.join()
print ("退出主线程")




