import threading
import time
def task():
    time.sleep(1)
    print(threading.current_thread())

if __name__ == '__main__':
    for i in range(5):
        thread = threading.Thread(target=task)
        thread.start()
