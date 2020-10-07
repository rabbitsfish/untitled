import time
print(time.asctime())
print(time.time())
print(time.localtime())
now = time.time()

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now - 60*60*24*3)))