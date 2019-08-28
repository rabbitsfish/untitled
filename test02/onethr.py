import time
import _thread
def loop0():
    print('start loop0 at:' ,time.ctime())
    time.sleep(4)
    print('start loop0 at:', time.ctime())

def loop1():
    print('start loop1 at:', time.ctime())
    time.sleep(2)
    print('start loop1 at:', time.ctime())

def main():
    print('start main at:', time.ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    time.sleep(6)
    print('start main at:', time.ctime())

if __name__ == '__main__':
    main()
