import pytest
# @pytest.mark.parametrize('test_a', [1, 2, 3])
# @pytest.mark.parametrize('test_b', [4, 5, 6])
# @pytest.mark.parametrize('excepted', [5, 7, 9])
# def test_sum(test_a, test_b, excepted):
#     sum = test_a + test_b
#     assert sum == excepted

# @pytest.fixture(params=[1, 2, 3])
# def data(request):
#     return request.param
#
# def test_01(data):
#     assert data == 1
test_user_data = ['Tome', 'jerry']
@pytest.fixture(scope='module')
def login(request):
    print(request.param)
    return request.param

@pytest.mark.parametrize("login", test_user_data, indirect=True)
def test_01(login):
    print(login + ".....")
    assert 1 != 1
