import _thread
import time
loops = [2, 4]
def loop(nloop, nsec, lock):
    print('start loop', nloop, 'at:', time.ctime())
    time.sleep(nsec)
    print('start loop', nloop, 'at:', time.ctime())
    lock.release()

def main():
    print('starting at:', time.ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked:
            pass

    print('all done at:', time.ctime())

if __name__ == '__main__':
    main()
