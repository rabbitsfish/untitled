import time
import threading

count = 0
thread_tasks = 100000
thread_tasks_num = 10
lock = threading.Lock()
def download():
    global count
    for i in range(thread_tasks):
        lock.acquire()
        count += 1
        lock.release()

threads = []

for i in range(thread_tasks_num):
    t = threading.Thread(target=download)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("count:", count)