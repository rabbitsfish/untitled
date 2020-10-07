import pytest
@pytest.mark.login
def test_01():
    print('test_01')


@pytest.mark.login
def test_02():
    print('test_02')

@pytest.mark.login1
def test_03():
    print('test_03')

@pytest.mark.login1
def test_04():
    print('test_04')

def test_05():
    print('test_05')