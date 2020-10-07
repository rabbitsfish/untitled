import logging
import time
import multiprocessing
import _thread
import threading
logging.basicConfig(level=logging.INFO)
loops = [2, 4]
def loop(nloop, nsec):
    logging.info("start loop " + str(nloop) + " " + time.ctime())
    time.sleep(nsec)
    logging.info("end loop " + str(nloop) + " " + time.ctime())
    # lock.release()

def main():
    logging.info("start all at " + time.ctime())
    locks = []
    nloops = range(len(loops))
    # for i in nloops:
    #     lock = _thread.allocate_lock()
    #     lock.acquire()
    #     locks.append(lock)
    threads = []
    for i in nloops:
        # _thread.start_new_thread(loop, (i, loops[i], locks[i]))
        threads.append(threading.Thread(target=loop, args=(i, loops[i])))

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()


    for i in locks:
        while i.locked():
            pass

    logging.info("end all at " + time.ctime())

if __name__ == '__main__':
    main()
