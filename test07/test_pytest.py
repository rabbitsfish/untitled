import pytest

@pytest.fixture(scope='function', autouse=True)
def login():
    print('login.....')
    yield
    print('login again')

def setup_module():
    print('for setup module')

def teardown_module():
    print('for teardown module')

def setup_function():
    print('for setup function')

def teardown_function():
    print('for teardown function')

def test_01():
    print("for test_01")
    x = 'This'
    assert 'h' in x

def test_02():
    print("for test_02")
    x = 'hello'
    assert 'e' in x
    pytest.assume('e' in x)

def test_03(login):
    print("for test_03")
    x = 'ello'
    y = 'hello world'
    assert x in y

class TestDemo():
    @classmethod
    def setup_class(cls):
        print('for setup_class')
    @classmethod
    def teardown_class(cls):
        print('for teardown_class')

    def setup_method(self):
        print('for setup_method')

    def teardown_method(self):
        print('for teardown_method')

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def test_demo_01(self):
        print('for test_demo_01')
        x = 'This'
        assert 'h' in x

    def test_demo_02(self, login):
        print('for test_demo_02')
        x = 'ello'
        y = 'hello world'
        assert x in y


    def test_demo_03(self, login):
        print('for test_demo_03')
        x = 'ello'
        y = 'hello world'
        assert x in y

if __name__ == '__main__':
    pytest.main("-v -s test_pytest.py::TestDemo")