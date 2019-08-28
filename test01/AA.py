class ShortForStrException(Exception):
    def __init__(self, length):
        self.length = length

def get_raise_exception():
    try:
        name = input('please enter a string:')
        if len(name) < 4:
            raise ShortForStrException(len(name))
    except Exception as result:
        print('the exception is ', result)
        raise

if __name__ == '__main__':
    get_raise_exception()