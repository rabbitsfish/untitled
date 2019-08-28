def w(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        count = 0
        while True:
            print('count:', count)
            if result:
                return True
            elif count > 5:
                return False
            else:
                result = func(*args, **kwargs)
                if count == 3:
                    result = True
                count += 1
    return inner
@w
def test1(*args, **kwargs):
    print('test1')
    return False

test1()