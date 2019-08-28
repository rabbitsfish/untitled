import threading
from queue import Queue
import time
class Product(threading.Thread):
    def __init__(self, queue, name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.name = name

    def run(self):
        while True:
            if not self.queue.full():
                self.queue.put('xxx')
                print('%s生产了一个苹果，总共有%d个苹果' % (self.name, self.queue.qsize()))
                time.sleep(3)

class Customer(threading.Thread):
    def __init__(self, queue, name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.name = name

    def run(self):
        while True:
            if not self.queue.empty():
                self.queue.get('xxx')
                print('%s吃了一个苹果，还剩下%d个苹果' % (self.name, self.queue.qsize()))
                time.sleep(3)


q = Queue(30)
threads = []
for i in range(5):
    threads.append(Product(q, '%d号' % i))
for i in range(5):
    threads.append(Customer(q, '%d号' % i))
for i in threads:
    i.start()