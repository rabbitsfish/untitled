import threading
import time

ticket = 10
lock = threading.Lock()
def sale_ticket():
   global ticket
   while ticket > 0:
       if lock.acquire():
           if ticket > 0:
               print(threading.current_thread().getName(), ':%s号票已经售出' % str(ticket))
               ticket -= 1
               time.sleep(1)
           else:
               print('票都没有了')
           lock.release()

def main():

    c1 = threading.Thread(target=sale_ticket, name='窗口1')
    c2 = threading.Thread(target=sale_ticket, name='窗口2')
    c1.start()
    c2.start()
    start = time.clock()
    elapsed = (time.clock() - start)
    print("程序耗时:", elapsed)

if __name__ == '__main__':
    main()
