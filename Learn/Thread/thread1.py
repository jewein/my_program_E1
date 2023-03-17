import threading

# 共享资源
shared_resource = 0

# 创建互斥锁
lock = threading.Lock()

def increment():
    global shared_resource

    # 获取互斥锁
    # lock.acquire()
    try:
        # 访问共享资源
        shared_resource += 1
    finally:
        # 释放互斥锁
        # lock.release()
        pass

# 创建多个线程并启动
threads = []
for _ in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

# 输出结果
print(f'Shared resource: {shared_resource}')
