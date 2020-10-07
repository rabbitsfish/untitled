import time


# 函数运行 2秒
def timeit(func):
    def result():
        start_time = time.time()
        func()
        end_time = time.time()
        print('函数运行时间为：%.2fs' % (end_time - start_time))

    return result

@timeit
def t_func():
    time.sleep(2)

print(t_func())