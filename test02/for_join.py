import threading, time

count = 10
def doWaiting0():
    global count
    while count > 0:
        print('start waiting0: ' + time.strftime('%H:%M:%S') + 'count:' + str(count))
        time.sleep(3)
        print('stop waiting0: ' + time.strftime('%H:%M:%S') + 'count:' + str(count))
        count -= 1

def doWaiting1():
    global count
    while count > 0:
        print('start waiting1: ' + time.strftime('%H:%M:%S') + 'count:' + str(count))
        time.sleep(8)
        print('stop waiting1: ', time.strftime('%H:%M:%S') + 'count:' + str(count))
        count -= 1

tsk = []
thread1 = threading.Thread(target = doWaiting0)
thread1.start()
tsk.append(thread1)
thread2 = threading.Thread(target = doWaiting1)
thread2.start()
tsk.append(thread2)
print('start join: ' + time.strftime('%H:%M:%S'))
for tt in tsk:
    print('to join')
    tt.join()
    print('join')
print('end join: ' + time.strftime('%H:%M:%S'))